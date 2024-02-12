#include <WiFi.h>
#include <PubSubClient.h>
#include "ICM_20948.h" // Get the library at http://librarymanager/All#SparkFun_ICM_20948_IMU

// Uncomment the following line to use SPI instead of I2C
// #define USE_SPI

#define SERIAL_PORT Serial

#ifdef USE_SPI
  #define SPI_PORT SPI
  #define CS_PIN 2
#else
  #define WIRE_PORT Wire
  #define AD0_VAL 1 // Change based on the I2C address bit
#endif

// WiFi credentials
const char ssid = "Christophe's iPhone";
const char password = "christophe";

// MQTT Broker settings
const char* mqtt_broker = "mqtt.eclipseprojects.io";
const char* topic = "ece180d/test";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

#ifdef USE_SPI
ICM_20948_SPI myICM; // SPI object
#else
ICM_20948_I2C myICM; // I2C object
#endif

void setup() {
  SERIAL_PORT.begin(115200);
  
  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    SERIAL_PORT.println("Connecting to WiFi..");
  }
  SERIAL_PORT.println("Connected to the WiFi network");
  
  // Connect to MQTT Broker
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);
  while (!client.connected()) {
    String client_id = "esp32-client-";
    client_id += String(WiFi.macAddress());
    SERIAL_PORT.printf("The client %s connects to the mqtt broker\n", client_id.c_str());
    if (client.connect(client_id.c_str())) {
      SERIAL_PORT.println("mqtt broker connected");
    } else {
      SERIAL_PORT.print("failed with state ");
      SERIAL_PORT.print(client.state());
      delay(2000);
    }
  }
  client.publish(topic, "Hi I’m ESP32 ^^");
  client.subscribe(topic);

  // Initialize sensor
  #ifdef USE_SPI
  SPI_PORT.begin();
  myICM.begin(CS_PIN, SPI_PORT);
  #else
  WIRE_PORT.begin();
  WIRE_PORT.setClock(400000);
  myICM.begin(WIRE_PORT, AD0_VAL);
  #endif

  bool initialized = false;
  while (!initialized) {
    SERIAL_PORT.print(F("Initialization of the sensor returned: "));
    SERIAL_PORT.println(myICM.statusString());
    if (myICM.status != ICM_20948_Stat_Ok) {
      SERIAL_PORT.println("Trying again...");
      delay(500);
    } else {
      initialized = true;
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  SERIAL_PORT.print("Message arrived in topic: ");
  SERIAL_PORT.println(topic);
  SERIAL_PORT.print("Message:");
  for (int i = 0; i < length; i++) {
    SERIAL_PORT.print((char)payload[i]);
  }
  SERIAL_PORT.println();
  SERIAL_PORT.println("-----------------------");
}

void loop() {
  if (myICM.dataReady()) {
    myICM.getAGMT(); // Update sensor data
    printScaledAGMT(&myICM); // Print scaled data
    client.loop();
    delay(30);
  } else {
    SERIAL_PORT.println("Waiting for data");
    client.loop();
    delay(500);
  }
}

void printPaddedInt16b(int16_t val) {
  if (val >= 0) SERIAL_PORT.print(" ");
  SERIAL_PORT.print(val < 0 ? "-" : "");
  for (int32_t div = 10000; div > 1; div /= 10) {
    if (abs(val) < div) SERIAL_PORT.print("0");
  }
  SERIAL_PORT.println(abs(val));
}

void printFormattedFloat(float val, uint8_t leading, uint8_t decimals) {
  char format[10];
  snprintf(format, sizeof(format), "%%%s%d.%df", val < 0 ? "-" : " ", leading + decimals + (val < 0 ? 1 : 2), decimals);
  SERIAL_PORT.printf(format, val);
}

#ifdef USE_SPI
void printScaledAGMT(ICM_20948_SPI *sensor) {
#else
void printScaledAGMT(ICM_20948_I2C *sensor) {
#endif
  // Print scaled acceleration, gyroscope, magnetometer, and temperature data
  SERIAL_PORT.print("Scaled. Acc (mg) [ ");
  printFormattedFloat(sensor->accX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->accY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->accZ(), 5, 2);
  SERIAL_PORT.print(" ], Gyr (DPS) [ ");
  printFormattedFloat(sensor->gyrX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->gyrY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->gyrZ(), 5, 2);
  SERIAL_PORT.print(" ], Mag (uT) [ ");
  printFormattedFloat(sensor->magX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->magY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->magZ(), 5, 2);
  SERIAL_PORT.print(" ], Tmp (C) [ ");
  printFormattedFloat(sensor->temp(), 5, 2);
  SERIAL_PORT.println(" ]");
}
