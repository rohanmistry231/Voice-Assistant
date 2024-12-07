import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import shutil
import pyautogui
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import datetime
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("own 1 point o")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.1)
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('userid@gmail.com', 'your password')
    server.sendmail('userid700@gmail.com', to, content)
    server.close()


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == '__main__':
    def clear(): return os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    # clear()
    # wishMe()
    # username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        # Command to open any website :
        if 'open youtube' in query:
            from open import opcommand
            opcommand(query)
        elif 'open google' in query:
            from open import opcommand
            opcommand(query)
        elif 'open stackoverflow' in query:
            from open import opcommand
            opcommand(query)
        # command to play song of our system :
        elif "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\Rohan S Mistry\\Music"  # "C:\\Users\\OWN\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
        # command to get the time of our system :
        elif 'the time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {current_time}")
        # command to open any application of our system :
        elif 'Youtube Music' in query:
            codePath = r"C:\\Users\\Rohan S Mistry\AppData\\Local\\Programs\\youtube-music-desktop-app\\YouTube Music Desktop App.exe"
            os.startfile(codePath)
        elif 'vs code' in query:
            codePath = r"C:\\Users\\Rohan S Mistry\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        # command for sending email to a user :
        elif "email to user" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("to Whom i send email?")
                new_to = takeCommand()  # "rohanmistry231@gmail.com"
                to = new_to.replace(" ", "")
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        # command for sending email to particular gmail-id :
        elif 'email to mama' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pritesh_02@yahoo.com"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        # command for communication with voice assistant :
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by ROHAN.")
        # command for telling jokes :
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        # frequently asked questions with voice assistant :
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        elif "why you came to world" in query:
            speak("Thanks to ROHAN. further It's a secret")
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\ROHAN\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I am your virtual assistant created by ROHAN")
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister ROHAN ")
        # changing background of screen and lockscreen :
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, "C:\\Users\\Rohan S Mistry\\OneDrive\\Pictures\\pubg.png", 0)
            speak("Background changed successfully")
        elif 'lock screen' in query:
            os.system('reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\Personalization /v LockScreenImage /t REG_SZ /d "{}" /f'.format(
                "C:\\Users\\Rohan S Mistry\\OneDrive\\Desktop\\gh.png"))
            speak("Background changed successfully")
        # most of system comm :
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif 'clear recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        # command for making notes and showing notes :
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('rohan.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                file.write(current_time)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show note" in query:
            speak("Showing Notes")
            file = open("rohan.txt", "r")
            print(file.read())
            speak(file.read(6))
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
        elif "i love you" in query:
            speak("It's hard to understand")
        # Shortcut commands
        elif "select all" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "copy" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "cut" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "past" in query or "paste" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "pause" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "resume" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "forward" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "backward" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "change window" in query:
            from chrome_shortcut import chrome_short
            chrome_short(query)
        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("3WR2KP-4U9X329R9U")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
        # command for any application shortcuts :
        elif "open new tab" in query:
            pyautogui.hotkey('ctrl', 't')
            speak("opening new tab")
        elif "close tab" in query:
            pyautogui.hotkey('ctrl', 'w')
            speak("closing new tab")
        elif "open new window" in query:
            pyautogui.hotkey('ctrl', 'n')
            speak("opening new window")
        elif "open history" in query:
            pyautogui.hotkey('ctrl', 'h')
            speak("opening history")
        # searching command :
        elif "google" in query:
            from GreetMe import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from GreetMe import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from GreetMe import searchWikipedia
            searchWikipedia(query)
        # to open and close apps :
        elif "hey open" in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "hey close" in query:
            from Dictapp import closeappweb
            closeappweb(query)
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")
        elif "volume up" in query:
            from keyb import volumeup
            volumeup()
        elif "volume down" in query:
            from keyb import volumedown
            volumedown()
        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "")
            speak("You told me to remember that"+rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt", "r")
            speak("You told me to remember that" + remember.read())
        elif "news" in query:
            from NewsRead import latestnews
            latestnews()
        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()
        elif "calculate" in query:
            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate", "")
            query = query.replace("jarvis", "")
            Calc(query)
