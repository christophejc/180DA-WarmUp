import paho.mqtt.client as mqtt
import numpy as np
import uuid

# THIS ACTS AS THE BROKER FOR THE INDIVIDUAL PLAYERS 
brokerAddress = "host"
brokerPort = 1883
topic = "RPS"

# Flag to control the main loop
running = True

#storing the players moves
moves = {}
scores = {"scoreTie": 0}  # Initial dictionary with only ties tracked

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
    global score1
    global score2
    global scoreTie
    
    p1, move1 = list(moves.items())[0]
    p2, move2 = list(moves.items())[1]

    if move1 == move2:
        scores['scoreTie'] += 1
        result = "its a tie!"
    elif (move1 == "r" and move2 == "s") or (move1 == "p" and move2 == "r") or (move1 == "s" and move2 == "p"):
        scores[p1] = scores.get(p1, 0) + 1  # Increment or initialize player 1's score
        result = f"{p1} wins!"
    else:
        scores[p2] = scores.get(p2, 0) + 1  # Increment or initialize player 2's score
        result = f"{p2} wins!"

    print(result)
    display_results()

    # Reset player moves for the next round
    moves.clear()


def display_results():
    print("\nCurrent Results:")
    for player, score in scores.items():
        if player != 'scoreTie':  # Skip the tie score for player-specific display
            print(f"{player}: {score} Wins")
    # Display ties
    print(f"Ties: {scores['scoreTie']}")

# Add additional client options (security, certifications, etc.)
# Many default options should be good to start off.

# Add callbacks to the client.
client_id = f"central-broker-{uuid.uuid4()}"
client = mqtt.Client(client_id=client_id)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')

# Call one of the loop*() functions to maintain network traffic flow with the broker.


try:
    client.loop_start()
    while running:
        pass

except KeyboardInterrupt:
    running = False
    print("goodbye...")

finally:
# Use disconnect() to disconnect from the broker.
    client.loop_stop()
    client.disconnect()