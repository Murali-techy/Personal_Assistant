import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hai udal ")

def wishme():
    hour = int(datetime.now().hour)  # Access hour attribute directly
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hey Amigo, do you need help?")

def takecommand():
    #activating microphone to take input
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
      print("Listening....")
      r.pause_threshold = 1
      audio=r.listen(source)
    try:
      print("recognizing....")
      query=r.recognize_google(audio,language="en-in")
      print("user said:",query)
    except Exception as e:
      print(e)
      speak("say that again please ....")
      return "none"
    return query


if __name__=='__main__':
    wishme()
    if 1:
      
      query=takecommand().lower()
      if 'wikipedia' in query:
        speak('What do you want to search on Wikipedia, sir?')
        summary = wikipedia.summary(query, sentences=2)
        print(f"Summary of {query}:\n{summary}")
        speak(f"Summary of {query}:\n{summary}")
      elif 'open youtube' in query:
        webbrowser.open("youtube.com")
      elif 'open google' in query:
        webbrowser.open("google.com")
      elif 'open notepad' in query:
        npath='c:\\Windows\\System32\\notepad.exe'
        os.startfile(npath)
      elif 'open command prompt' in query:
        os.system('start cmd')
      elif 'time' in query:
        strTime=datetime.now().strftime("%H....%M....")
        speak(f"Time is{strTime}")
      else:
        speak("thank u , have a good day")
sys.exit()