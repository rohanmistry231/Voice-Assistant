import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def opcommand(query):
    if 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")
    elif 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif 'open facebook' in query:
        speak("Here you go to Facebook\n")
        webbrowser.open("facebook.com")
    elif 'open twitter' in query:
        speak("Here you go to twitter")
        webbrowser.open("twitter.com")
    elif 'open wikipedia' in query:
        speak("Here you go to wikipedia\n")
        webbrowser.open("wikipedia.com")
    elif 'open instagram' in query:
        speak("Here you go to instagram\n")
        webbrowser.open("instagram.com")
    elif 'open Baidu' in query:
        speak("Here you go to buidu\n")
        webbrowser.open("baidu.com")
    elif 'open yahoo' in query:
        speak("Here you go to yahoo\n")
        webbrowser.open("yahoo.com")
    elif 'open yandex' in query:
        speak("Here you go to yandex\n")
        webbrowser.open("yandex.ru")
    elif 'open whatsapp' in query:
        speak("Here you go to whatsapp\n")
        webbrowser.open("whatsapp.com")
    elif 'open amazone' in query:
        speak("Here you go to amazone\n")
        webbrowser.open("amazone.com")
    elif 'open zoom' in query:
        speak("Here you go to zoom\n")
        webbrowser.open("zoom.us")
    elif 'open live' in query:
        speak("Here you go to live\n")
        webbrowser.open("live.com")
    elif 'open netflix' in query:
        speak("Here you go to netflix\n")
        webbrowser.open("netflix.com")
    elif 'open yahoo.co.jp' in query:
        speak("Here you go to yahoo\n")
        webbrowser.open("yahoo.co.jp")
    elif 'open ' in query:
        speak("Here you go to \n")
        webbrowser.open(".com")
    elif 'open vk' in query:
        speak("Here you go to vk\n")
        webbrowser.open("vk.com")
    elif 'open reddit' in query:
        speak("Here you go to reddit\n")
        webbrowser.open("reddit.com")
    elif 'open office' in query:
        speak("Here you go to office\n")
        webbrowser.open("office.com")
    elif 'open naver' in query:
        speak("Here you go to naver\n")
        webbrowser.open("naver.com")
    elif 'open pinterest' in query:
        speak("Here you go to pinterest\n")
        webbrowser.open("pinterest.com")
    elif 'open discord' in query:
        speak("Here you go to discord\n")
        webbrowser.open("discord.com")
    elif 'open linkedin' in query:
        speak("Here you go to linkedin\n")
        webbrowser.open("linkedin.com")
    elif 'open cnn' in query:
        speak("Here you go to cnn\n")
        webbrowser.open("cnn.com")
    elif 'open microsoft' in query:
        speak("Here you go to microsoft\n")
        webbrowser.open("microsoft.com")
    elif 'open mail' in query:
        speak("Here you go to mail\n")
        webbrowser.open("mail.ru")
    elif 'open globo' in query:
        speak("Here you go to globo\n")
        webbrowser.open("globo.com")
    elif 'open bing' in query:
        speak("Here you go to bing\n")
        webbrowser.open("bing.com")
    elif 'open twitch' in query:
        speak("Here you go to twitch\n")
        webbrowser.open("twitch.tv")
    elif 'open google.com.br' in query:
        speak("Here you go to google\n")
        webbrowser.open("google.com.br")
    elif 'open qq' in query:
        speak("Here you go to qq\n")
        webbrowser.open("qq.com")
    elif 'open microsoftonline' in query:
        speak("Here you go to microsoftonline\n")
        webbrowser.open("microsoftonline.com")
    elif 'open ebay' in query:
        speak("Here you go to ebay\n")
        webbrowser.open("ebay.com")
    elif 'open msn' in query:
        speak("Here you go to msn\n")
        webbrowser.open("msn.com")
    elif 'open news.yahoo.co.jp' in query:
        speak("Here you go to news.yahoo.co.jp\n")
        webbrowser.open("news.yahoo.co.jp.com")
    elif 'open duckduckgo' in query:
        speak("Here you go to duckduckgo\n")
        webbrowser.open("duckduckgo.com")
    elif 'open ok' in query:
        speak("Here you go to ok\n")
        webbrowser.open("ok.ru")
    elif 'open walmart' in query:
        speak("Here you go to walmart\n")
        webbrowser.open("walmart.com")
    elif 'open bilibili' in query:
        speak("Here you go to bilibili\n")
        webbrowser.open("bilibili.com")
    elif 'open tiktok' in query:
        speak("Here you go to tiktok\n")
        webbrowser.open("tiktok.com")
    elif 'open paypal' in query:
        speak("Here you go to paypal\n")
        webbrowser.open("paypal.com")
    elif 'open google.de' in query:
        speak("Here you go to google.de\n")
        webbrowser.open("google.de")
    elif 'open amazon.co.jp' in query:
        speak("Here you go to amazon.co.jp\n")
        webbrowser.open("amazon.co.jp")
    elif 'open aliexpress' in query:
        speak("Here you go to aliexpress\n")
        webbrowser.open("aliexpress.com")
    elif 'open amazone.de' in query:
        speak("Here you go to amazone.de\n")
        webbrowser.open("amazone.de")
    elif 'open rakuten.co.jp' in query:
        speak("Here you go to rakuten.co.jp\n")
        webbrowser.open("rakuten.co.jp")
    elif 'open amazon.co.uk' in query:
        speak("Here you go to amazon.co.uk\n")
        webbrowser.open("amazon.co.uk")
