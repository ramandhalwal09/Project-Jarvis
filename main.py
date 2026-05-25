import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "45372b97d1a24fbaa8ffeb8066d1537e"

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()
    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')
    # Play the MP3 file
    pygame.mixer.music.play()
    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    
    elif "open linkedin" in c.lower():
        webbrowser.open("http://in.linkedin.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("http://www.youtube.com")

    elif "open w3schools" in c.lower():
        webbrowser.open("http://www.w3schools.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclib.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=45372b97d1a24fbaa8ffeb8066d1537e")
        if r.status_code == 200:
            data = r.json()
            articles = data["articles"]
            for article in articles:
                print(article["title"])

if __name__ == "__main__" :
    speak("Initializing Jarvis......")
    # Listen for the wake word "Jarvis"
    while True :
        # Obtain audio from microphone
        r = sr.Recognizer()
        
        print("recognizing....")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening......")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            Word = r.recognize_google(audio)
            if (Word.lower() == "jarvis"):
                speak("I am listening")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active......")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=2, phrase_time_limit=2)
                    command = r.recognize_google(audio)

                    ProcessCommand(command)

        except Exception as e:
            print("Error!; {0}".format(e))
