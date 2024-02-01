import paho.mqtt.client as mqtt
import numpy as np

# THIS ACTS AS THE BROKER FOR THE INDIVIDUAL PLAYERS 
brokerAddress = "host"
brokerPort = 1883
topic = "RPS"

#storing the players moves
name = "Enter name: "


# Callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# Callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def player_move ():
    while True:
        move = input("Rock [r], Paper [p], or Scissors [s] ?\n")
        if move in ["r", "p", "s"]:
            return move
        else:
            print("Invalid input! Rock [r], Paper [p], or Scissors [s] ?\n")




# Create a client instance.
client = mqtt.Client(name)

# Add additional client options (security, certifications, etc.)
# Many default options should be good to start off.

# Add callbacks to the client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')

# Call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

try:
    while True:
        move = player_move()
        client.publish(topic, f"{name},{move}")

except KeyboardInterrupt:
    print("goodbye...")

finally:
# Use disconnect() to disconnect from the broker.
    client.loop_stop()
    client.disconnect()