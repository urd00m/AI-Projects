
# Python program to show
# how to convert text to speech
import pyttsx3
  
# Initialize the converter
converter = pyttsx3.init()


voices = converter.getProperty('voices')
  
for i in range(len(voices)):
    voice = voices[i]

    # to get the info. about various voices in our PC 
    print("Voice:")
    print(i)
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)
    converter.setProperty('voice', voices[i].id)
    converter.say("Hello GeeksforGeeks")
    converter.say("I'm also a geek")
    converter.runAndWait()
