import pyttsx3
import speech_recognition as sr

# Initialising
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)

# constants
NAME = "Thahir"

engine.say(f"Hello, {NAME}. What do you want me to do?")
engine.runAndWait()
while True:
    print("Say Something: ")
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)

        #listens for the user's input
        audio2 = r.listen(source2)

		# Using google to recognize audio
        try:
            prompt = r.recognize_google(audio2)
        except:
            prompt = ""
        prompt = prompt.lower()
    if 'hello' in prompt:
        engine.say("Hello To You Too")
        engine.runAndWait()
    elif 'how are you' in prompt:
        engine.say("I am Fine, Thanks for asking")
        engine.runAndWait()
    elif 'goodbye' in prompt:
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
    elif 'say'in prompt:
        engine.say(f"What do you want me to say: ")
        engine.runAndWait()
        print("Say: ")
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)

            #listens for the user's input
            audio2 = r.listen(source2)

		    # Using google to recognize audio
            saying = r.recognize_google(audio2)
            saying = saying.lower()
        
        engine.say(f"You Said: {saying}")
        engine.runAndWait()
    else:
        engine.say("Huh! I Didn't Understand That.")
        engine.runAndWait()