import paho.mqtt.client as mqtt
import numpy as np

# THIS ACTS AS THE BROKER FOR THE INDIVIDUAL PLAYERS 
brokerAddress = "host"
brokerPort = 1883
topic = "RPS"

#storing the players moves
moves = {}


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

# Default message callback.
# (won’t be used if only publishing, but can still exist)
def on_message(client, userdata, message):
    players, currentMove = message.payload.decode().split(",")
    moves[players] = currentMove
    
    if len(moves) == 2:
       winner() 

def winner ():
    p1, move1 = list(moves.items())[0]
    p2, move2 = list(moves.items())[1]

    if move1 == move2:
        result = "its a tie!"
    elif (move1 == "r" and move2 == "s") or (move1 == "p" and move2 == "r") or (move1 == "s" and move2 == "p"):
        result = f"{p1} wins!"
    else:
        result = f"{p2} 2 wins!"

    print(result)

    # Reset player moves for the next round
    moves.clear()


# Create a client instance.
client = mqtt.Client()

# Add additional client options (security, certifications, etc.)
# Many default options should be good to start off.

# Add callbacks to the client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')

# Call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

try:
    while True:
        pass

except KeyboardInterrupt:
    print("goodbye...")

finally:
# Use disconnect() to disconnect from the broker.
    client.loop_stop()
    client.disconnect()
