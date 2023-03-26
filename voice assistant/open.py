import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def opcommand(query):
    if 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")