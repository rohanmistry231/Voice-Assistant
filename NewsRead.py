import speech_recognition as sr
import requests
import json
import pyttsx3


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.1)
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def latestnews():
    api_dict = {"business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1a1ac9b8505341478289bc11a04eb056",
                "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=1a1ac9b8505341478289bc11a04eb056",
                "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=1a1ac9b8505341478289bc11a04eb056",
                "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=1a1ac9b8505341478289bc11a04eb056",
                "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=1a1ac9b8505341478289bc11a04eb056",
                "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=1a1ac9b8505341478289bc11a04eb056"
                }

    content = None
    url = None
    speak(
        "Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("thats all")
