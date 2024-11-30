import os
import datetime
import time
import subprocess
import smtplib
import ctypes
import shutil
import pyttsx3
import speech_recognition as sr
import pyjokes
import pyautogui
from ecapture import ecapture as ec
from urllib.request import urlopen
import wolframalpha


# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you?")

def take_command():
    """Listen to user input and return the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I did not understand. Please repeat.")
        return "None"
    return query.lower()

def send_email(to, content):
    """Send an email to the specified address."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')  # Replace with your credentials
        server.sendmail('your_email@gmail.com', to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        print(e)
        speak("Failed to send email.")

def play_music():
    """Play music from the default directory."""
    music_dir = "C:\\Users\\YourUsername\\Music"  # Update this path
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
    else:
        speak("No music files found.")

def set_alarm(time_str):
    """Set an alarm."""
    with open("Alarmtext.txt", "w") as alarm_file:
        alarm_file.write(time_str)
    speak("Alarm is set.")

def get_current_time():
    """Return the current time."""
    return datetime.datetime.now().strftime("%I:%M %p")

def handle_query(query):
    """Process the query and execute the relevant command."""
    if 'open youtube' in query:
        os.system("start https://youtube.com")
    elif 'open google' in query:
        os.system("start https://google.com")
    elif 'play music' in query:
        play_music()
    elif 'the time' in query:
        current_time = get_current_time()
        speak(f"The time is {current_time}")
    elif 'send email' in query:
        speak("What should I say?")
        content = take_command()
        speak("To whom should I send it?")
        to = take_command().replace(" ", "").lower()
        send_email(to, content)
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    elif 'take a photo' in query:
        ec.capture(0, "Camera", "img.jpg")
    elif 'shutdown system' in query:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
    elif 'restart system' in query:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")
    elif 'lock window' in query:
        ctypes.windll.user32.LockWorkStation()
    elif 'hibernate' in query:
        speak("Hibernating the system.")
        os.system("shutdown /h")
    elif 'write a note' in query:
        speak("What should I write?")
        note = take_command()
        with open("Notes.txt", "w") as note_file:
            note_file.write(note)
        speak("Note written successfully.")
    elif 'show note' in query:
        try:
            with open("Notes.txt", "r") as note_file:
                notes = note_file.read()
                print(notes)
                speak(notes)
        except FileNotFoundError:
            speak("No notes found.")
    elif 'alarm' in query:
        speak("Please provide the alarm time in HH:MM format.")
        alarm_time = input("Alarm time (HH:MM): ")
        set_alarm(alarm_time)
    elif 'search' in query:
        speak("What should I search?")
        search_query = take_command()
        os.system(f"start https://google.com/search?q={search_query}")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("I am not sure how to help with that.")

if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command()
        handle_query(query)
