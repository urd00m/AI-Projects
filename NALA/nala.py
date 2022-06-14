import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys
import subprocess
import tempfile
import os
import time
import pyautogui
import osascript

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
        talk("nala shutdown")
        sys.exit(0)
    elif(userinput == "new terminal"):
        subprocess.call(['open', '-n', '-a', 'Terminal.app'])
    elif(userinput == "new workspace"):
        code,out,err = osascript.run('tell app "Terminal" to do script "cd ~/Desktop\nsay online\nworkspace_bringup\nclear" activate')
    elif(userinput == "jump"):
        pyautogui.write("jump\n")
    elif("nala sleep" in userinput):
        os.system("pmset sleepnow")
    elif(userinput == "top"):
        code,out,err = osascript.run('tell app "Terminal" to do script "top" activate')


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
