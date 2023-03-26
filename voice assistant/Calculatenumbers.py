import wolframalpha
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "api-key"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        result = f"The answer is {result}"
        print(result)
        speak(result)

    except:
        speak("The value is not answerable")

# command to calculate values another :		
		# elif "calculate" in query:
		# 	app_id = "3WR2KP-4U9X329R9U"
		# 	client = wolframalpha.Client(app_id)
		# 	indx = query.lower().split().index('calculate')
		# 	query = query.split()[indx + 1:]
		# 	res = client.query(' '.join(query))
		# 	answer = next(res.results).text
		# 	print("The answer is " + answer)
		# 	speak("The answer is " + answer)