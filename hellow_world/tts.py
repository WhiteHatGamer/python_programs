import pyttsx3
import speech_recognition as sr

# Initialising
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

# constants
NAME = "Thahir"
exit_commands = ["goodbye", "bye", "exit"]
hello_commands = ["hello", "hi", "hey", "howdy", "salaam", "greetings"]

engine.say(f"Hello, {NAME}. What do you want me to do?")
engine.runAndWait()
while True:
    print("Say Something: ")
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)

        #listens for the user's input
        # TODO: Add Timout feature
        audio2 = r.listen(source2)

		# Using google to recognize audio
        # TODO: Add Separate exception handling for better experience?
        try:
            prompt = r.recognize_google(audio2)
        except:
            prompt = ""
        prompt = prompt.lower()
    if any(command in prompt for command in hello_commands):
        engine.say("Hello To You Too")
        engine.runAndWait()
    elif 'how are you' in prompt:
        engine.say("I am Fine, Thanks for asking")
        engine.runAndWait()
    elif any(command in prompt for command in exit_commands):
        engine.say("Goodbye, have a nice day!")
        engine.runAndWait()
        break
    elif 'jarvis' in prompt:
        engine.setProperty('voice', voices[0].id)
        engine.say(f"Hello {NAME}, What do you want me to do")
        engine.runAndWait()
    elif 'friday' in prompt:
        engine.setProperty('voice', voices[1].id)
        engine.say(f"Hello {NAME}, What do you want me to do")
        engine.runAndWait()
    elif 'fast' in prompt:
        engine.setProperty(
            'rate',
            engine.getProperty('rate') + 10
            )
        engine.say("Hope this is Okay!!")
        engine.runAndWait()
    elif 'slow' in prompt:
        engine.setProperty(
            'rate',
            engine.getProperty('rate') - 10
            )
        engine.say("Hope this is Okay!!")
        engine.runAndWait()
    elif 'rate' in prompt:
        engine.say(f"Speech Rate is {engine.getProperty('rate')}")
        engine.runAndWait()
    elif 'ditto'in prompt:
        engine.say(f"Ditto Mode: ON, Say quit to turn off")
        engine.runAndWait()
        is_saying = True
        while is_saying:
            print("Say: ")
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                #listens for the user's input
                audio2 = r.listen(source2)

		        # Using google to recognize audio
                try:
                    saying = r.recognize_google(audio2)
                except:
                    saying = ""
                saying = saying.lower()
            if "quit" in saying:
                is_saying = False
                engine.say("Ditto Mode: OFF")
                engine.runAndWait()
            else:
                engine.say(f"{saying}")
                engine.runAndWait()

    else:
        engine.say("Huh! I Didn't Understand That.")
        engine.runAndWait()