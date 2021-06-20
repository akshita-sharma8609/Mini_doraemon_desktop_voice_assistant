"""============================================ PYTHON PROJECT: MINI DOAREMON - PERSONAL AI ASSISTANT ========================================="""

import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


'''Microsoft speech API for windows'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def greetuser():
    """This function greet the user according to time"""
    hour=datetime.datetime.now().hour
    if(hour>0 and hour <12):
        speak("Good Morning")
    elif(hour>=12 and hour<=18):
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am mini doramon, How can i help you?")


def takeinput():
    """This function take voice commands from user and convert them into text"""
    s=sr.Recognizer()#initializing the recognizer
    with sr.Microphone() as source:
        print("\nSay Something...")
        s.adjust_for_ambient_noise(source,duration=1)#adjust for ambient noise and help to take clear input
        s.pause_threshold = 1
        s.energy_threshold=500
        audio=s.listen(source)#listen the user input
    try:
        print("Recognizing...")
        text= s.recognize_google(audio,language='en-in')#recognize the user audio
        print(f"you said: {text}\n")
    except Exception as e:
        print("Say that again...")
        takeinput().lower()
    return text


def speak(audio):
    """This function converts text to speech"""
    engine=pyttsx3.init()#using init function to get an engine instance
    engine.say(audio)#say method on engine to pass audio to spoken
    engine.runAndWait()#It produces voice commands

if __name__=='__main__':
    greetuser()
    while True:

        try:
            query= takeinput().lower()
            browser_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if "introduction" in query or "about you" in query:
                speak("My name is mini doraymon, i am an AI desktop assistant and My developer is akshita sharma")

            elif ("who are you" in query) or  ( "your name" in query):
                speak("My name is mini doraemon, i am an AI desktop assistant")

            elif "how are you" in query :
                speak("I am fine,thank you,  Hope you are also doing well!")

            elif "wikipedia" in query:
                print('Searching Wikipedia...')
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif ("open google" in query) or ("google" in query):
                url='https://www.google.co.in/'
                c=webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get("chrome").open(url)

            elif ("open youtube" in query) or ("youtube" in query):
                url='https://www.youtube.com/'
                c=webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open(url)

            elif ("open stack overflow" in query) or ("open stackoverflow" in query) or ("open stack over flow" in query) or ("stackoverflow" in query):
                url='https://stackoverflow.com/'
                c=webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open(url)

            elif ("open vs code" in query) or ("open visual studio code" in query) or ("open vscode" in query) or ("vscode" in query):
                codepath="C:\\Users\\akshi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif ("open code blocks" in query) or  ("open codeblocks" in query):
                codepath="C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
                os.startfile(codepath)

            elif ("open github" in query) or  ("open git hub" in query) :
                url='https://github.com/'
                c=webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open(url)

            elif ("open mail" in query) or ("open email" in query) or ("open gmail" in query):
                url='https://gmail.com/'
                c=webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open(url)

            elif "time" in query:
                str_time=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is {str_time}")
                speak(f"The time is {str_time}")

            elif ('play music' in query) or ('music' in query):
                music_dir = 'C:\\Users\\akshi\\Music'
                songs = os.listdir(music_dir)
                var_music=random.randint(0,len(songs))
                os.startfile(os.path.join(music_dir, songs[var_music]))
            else:
                print("Results not found!")
        except Exception as e:
            print("Something went wrong")




