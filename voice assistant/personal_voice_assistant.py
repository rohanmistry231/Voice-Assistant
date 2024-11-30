"""
Personal Voice Assistant
"""

import os
import subprocess
import datetime
import ctypes
import time
import smtplib
import pyttsx3
import pyjokes
import shutil
import pyautogui
import speech_recognition as sr
from ecapture import ecapture as ec
from wolframalpha import Client
import winshell

# Initialize Text-to-Speech engine
ENGINE = pyttsx3.init('sapi5')
VOICES = ENGINE.getProperty('voices')
ENGINE.setProperty('voice', VOICES[0].id)

# Global Variables
ASSISTANT_NAME = "AI.01"
USER_NAME = "User"


def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def speak(text):
    """Convert text to speech."""
    ENGINE.say(text)
    ENGINE.runAndWait()


def wish_me():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"I am your assistant, {ASSISTANT_NAME}. How can I help you today?")


def get_user_name():
    """Ask the user for their name."""
    global USER_NAME
    speak("What should I call you?")
    USER_NAME = take_command().capitalize()
    speak(f"Welcome, {USER_NAME}!")
    print(f"Welcome, {USER_NAME}!".center(40, "#"))


def take_command():
    """
    Listen to the user's voice input and return it as text.
    Returns 'None' if the input cannot be recognized.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        try:
            audio = recognizer.listen(source, timeout=4)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Unable to recognize your voice.")
            return "None"
        except sr.RequestError as err:
            print(f"Error recognizing voice: {err}")
            return "None"


def send_email(receiver, content):
    """Send an email to the specified receiver with the given content."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')  # Replace with your credentials
        server.sendmail('your_email@gmail.com', receiver, content)
        server.quit()
        speak("Email has been sent successfully.")
    except Exception as err:
        print(f"Error: {err}")
        speak("Unable to send the email.")


def execute_query(query):
    """Process the user's command and execute the appropriate action."""
    if "open youtube" in query:
        os.system("start https://www.youtube.com")
    elif "open google" in query:
        os.system("start https://www.google.com")
    elif "play song" in query:
        play_song()
    elif "the time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "email to" in query:
        send_email_flow()
    elif "joke" in query:
        tell_joke()
    elif "write a note" in query:
        write_note()
    elif "show note" in query:
        read_note()
    elif "shutdown" in query:
        shutdown_system()
    elif "lock window" in query:
        lock_system()
    elif "camera" in query:
        take_photo()
    elif "exit" in query:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")


def play_song():
    """Play a random song from a specified directory."""
    music_dir = "D:\\Coding\\va\\voice_assistant\\"  # Change path as needed
    try:
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music.")
        else:
            speak("No songs found in the music directory.")
    except FileNotFoundError:
        speak("Music directory not found.")
    except Exception as error:
        print(f"Error playing music: {error}")
        speak("Unable to play music.")


def tell_joke():
    """Tell a random joke."""
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


def write_note():
    """Write a note to a file."""
    speak("What should I write?")
    note_content = take_command()
    speak("Should I include the date and time?")
    include_time = take_command()
    try:
        with open('notes.txt', 'a') as note_file:
            if 'yes' in include_time:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                note_file.write(f"{current_time}: {note_content}\n")
            else:
                note_file.write(f"{note_content}\n")
        speak("Note saved successfully.")
    except Exception as error:
        print(f"Error writing note: {error}")
        speak("Failed to save the note.")


def read_note():
    """Read and display notes from the notes file."""
    try:
        with open('notes.txt', 'r') as note_file:
            notes = note_file.read()
            print(notes)
            speak(notes)
    except FileNotFoundError:
        speak("No notes found.")
    except Exception as error:
        print(f"Error reading notes: {error}")
        speak("Unable to read notes.")


def send_email_flow():
    """Flow for sending an email."""
    speak("What should I say?")
    content = take_command()
    speak("To whom should I send it?")
    receiver = take_command().replace("at the rate", "@").replace(" ", "")
    send_email(receiver, content)


def take_photo():
    """Take a photo using the webcam."""
    try:
        ec.capture(0, "AI Assistant Camera", "img.jpg")
        speak("Photo taken successfully.")
    except Exception as err:
        print(f"Error: {err}")
        speak("Unable to access the camera.")


def shutdown_system():
    """Shut down the system."""
    speak("Shutting down the system.")
    os.system("shutdown /s /t 1")


def lock_system():
    """Lock the system."""
    speak("Locking the device.")
    ctypes.windll.user32.LockWorkStation()


if __name__ == "__main__":
    clear_console()
    wish_me()
    get_user_name()
    while True:
        user_query = take_command()
        if user_query != "None":
            execute_query(user_query)
