# Refereneces from: https://www.youtube.com/watch?v=9GJ6XeB-vMg for audio to text algorithm
import speech_recognition
import keyboard



recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    print("Speech recognition is active. Say 'quit' to exit.")
    while True:
        try:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized: {text}")

            # Check if 'q' key is pressed to exit
            if text == "quit":
                print("Exiting...")
                exit()

        except speech_recognition.UnknownValueError:
            print("Speech recognition could not understand audio.")
            recognizer = speech_recognition.Recognizer()
             


