import pyttsx3

# Initialising
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)

# constants
NAME = "Thahir"

engine.say(f"Hello, {NAME}. What do you want me to do?")
engine.runAndWait()
while True:
    prompt = (input("Say Something: ").lower())
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
    else:
        engine.say("Huh! I Don't Understand That yet...")
        engine.runAndWait()