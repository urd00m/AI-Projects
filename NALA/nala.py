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
import wikipedia
import pyjokes

global hibernate

# Functions
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with microphone as source:
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=2)
            userinput = listener.recognize_google(voice)
            userinput = userinput.lower()
    except:
        userinput = "none"
    return userinput

#### TODO: using in instead of == ####
def run_nala():
    global hibernate

    # User input
    userinput = take_command()
    print(userinput)

    # Hibernate
    if(hibernate == True and userinput != "hibernate"):
        return
    elif(hibernate == True and userinput == "hibernate"):
        hibernate = False
        return

    # Commands
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
    elif(userinput == "system status"):
        code,out,err = osascript.run('tell app "Terminal" to do script "top" activate')
    elif(userinput == 'joke'):
        talk(pyjokes.get_joke())
    elif('look up' in userinput):
         subprocess.call(['open', '-a', 'Safari.app', 'http://google.com'])
         try:
             userinput = userinput.split("look up")[-1]
         except:
             print("bad search")
             return
         time.sleep(.5)
         pyautogui.typewrite(userinput+"\n")
    elif('hibernate' == userinput):
        hibernate = True

# Init
listener = sr.Recognizer()
microphone = sr.Microphone()

# Calibrate
with microphone as source:
    listener.adjust_for_ambient_noise(source, duration=2)  # we only need to calibrate once, before we start listening

# Set up talking engine 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id) # 0 is us, 7 is british, 17 is aussie, 23 ar_SA, 45 YURI, 

# Display name
print(""" _   _   ___   _       ___  
| \\ | | / _ \\ | |     / _ \\ 
|  \\| |/ /_\\ \\| |    / /_\\ \\ 
| . ` ||  _  || |    |  _  | 
| |\  || | | || |____| | | | 
\\_| \\_/\\_| |_/\\_____/\\_| |_/ """)

# Var setup
hibernate = False

# run
while True:
    run_nala()
