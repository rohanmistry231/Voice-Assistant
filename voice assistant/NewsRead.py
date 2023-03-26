import speech_recognition as sr
import requests
import json
import pyttsx3
def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.adjust_for_ambient_noise(source,duration=0.1)
		r.energy_threshold = 300
		r.pause_threshold = 1 
		# What is pause thresold ? ans is given below.
		#A pause threshold value in a voice assistant refers to the length of time that the assistant will wait before ending a speech recognition session if there is a pause in the user's speech.
		#For example, if a pause threshold value is set to 2 seconds, and the user stops speaking for more than 2 seconds, the voice assistant will assume that the user has finished speaking and end the speech recognition session.
		#This feature is useful because it allows the voice assistant to accurately recognize when the user has finished speaking, and it can help to prevent false positives or misinterpretations of the user's speech.
		audio = r.listen(source,0,4)
                
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=api-key",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=api-key",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=api-key",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=api-key",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=api-key",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=api-key"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
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
    for articles in arts :
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