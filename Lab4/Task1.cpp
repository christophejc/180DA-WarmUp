#include <Wire.h>
#include <SparkFunMPU9250-DMP.h> 

MPU9250_DMP imu; 

void setup() {
  Serial.begin(115200); 
  Wire.begin(); 
  
  if (!imu.begin()) { 
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  
  imu.setAccelRange(MPU9250::ACCEL_RANGE_2G); 
  imu.setGyroRange(MPU9250::GYRO_RANGE_250DPS); 
}

void loop() {
  imu.readSensor(); 
  
  // accel data
  VectorFloat accel = imu.getAccel();
  Serial.print("Acceleration (m/s^2): X: ");
  Serial.print(accel.x, 2);
  Serial.print(", Y: ");
  Serial.print(accel.y, 2);
  Serial.print(", Z: ");
  Serial.println(accel.z, 2);
  
  // gyro data
  VectorFloat gyro = imu.getGyro();
  Serial.print("Gyroscope (deg/s): X: ");
  Serial.print(gyro.x, 2);
  Serial.print(", Y: ");
  Serial.print(gyro.y, 2);
  Serial.print(", Z: ");
  Serial.println(gyro.z, 2);
  
  delay(1000);
}