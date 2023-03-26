import speech_recognition as sr
import pyttsx3
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def chrome_short(query):
	if "select all" in query:
		speak("selecting all")
		pyautogui.hotkey('ctrl','a')
	elif "copy" in query:
		speak("copying successfully")
		pyautogui.hotkey('ctrl', 'c')
	elif "cut" in query:
		speak("pressing control x")
		pyautogui.hotkey('ctrl', 'x')
	elif "past" in query or "paste" in query:
		speak("pasting successfully")
		pyautogui.hotkey('ctrl', 'v')
	elif "pause" in query:
		speak("pausing video")
		pyautogui.press('space')
	elif "resume" in query:
		speak("resuming video")
		pyautogui.press('space')
	elif "forward" in query:
		speak("forwarding video")
		pyautogui.press('right')
	elif "backward" in query:
		speak("backwarding video")
		pyautogui.press('left')
	elif "change window" in query:
		speak("changin window")
		pyautogui.hotkey('alt','tab')