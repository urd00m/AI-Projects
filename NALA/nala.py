import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys

# Functions
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with microphone as source:
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=3)
            userinput = listener.recognize_google(voice)
            userinput = userinput.lower()
    except:
        userinput = "none"
    return userinput


def run_nala():
    userinput = take_command()
    print(userinput)
    if(userinput == "quit"):
        sys.exit(0)

# Init
listener = sr.Recognizer()
microphone = sr.Microphone()

# Calibrate
with microphone as source:
    listener.adjust_for_ambient_noise(source, duration=2)  # we only need to calibrate once, before we start listening

# Set up talking engine 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Display name
print(""" _   _   ___   _       ___  
| \\ | | / _ \\ | |     / _ \\ 
|  \\| |/ /_\\ \\| |    / /_\\ \\ 
| . ` ||  _  || |    |  _  | 
| |\  || | | || |____| | | | 
\\_| \\_/\\_| |_/\\_____/\\_| |_/ """)
                            
                            

# run
while True:
    run_nala()
