![Alt text](image.png)

MQTT:

Based on your experiences, what is made possible using MQTT? 

Using MQTT, communication between different devices on the same network becomes readily possible without having to worry about ip addresses, sockets or other caveats of network programming.

What seems fairly difficult using MQTT? If you were to use MQTT, what would be areasonable communications lag time be? Would you prefer to use a different method of transmitting data?

It seems difficult to do back and forth communication in real time seeing as there are publishers and subscribers that are distinguished, meaning it could be difficult for back and forth publishing and communicating without having potential latency issues. For more simple back and forth communication it is very fast and capable. 


SPEECH: 

(a) What can you do with your given speech program in the project?

I can recognize different words and phases that are separated by a long pause and have it transcribe. Especial with this "quit" functionality I can have specific words trigger action like exiting the program. For our Mini Golf Game it could be like using th espeech to choose different types of clubs or change the gravity of the course.

(b) How complex do you want your speech recognition to be? How complex can you reasonably expect your speech recognition to be?

I want the speech recognition to be complex enough to pick up on trigger words in the midst of a moderately noisey background environment (i.e the lab). I this this can be expected with creative programming and a quality microphone 

(c) What level of speech accuracy do you need? In other words, how quickly do you need an accurate recognition? Does a missed recognition hurt the progress of the game?

I need the speech to recognize speech in real time (within a second or two). A missed recognition may hurt the progress of a multiplayer game if we determine that time is an object of the competition

(d) Do you need specific hardware, specific conditions, etc. to have a reasonable confidence that it works well enough?

I think that using an actual microphone as opposed to one from a laptop is the biggest determination to see if it will work well enough, outside of that I am relatively confident because for noise that doesn't sound like specific words the program does not pick up on. So in a lab where all of the contrasting conversations sound like gibberish, it may still be successful