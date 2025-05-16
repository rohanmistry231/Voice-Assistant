import pyttsx3
import speech_recognition as sr
import datetime
from pathlib import Path
import spacy
import logging
from modules import chrome_shortcut, search, apps, keyboard, news, calculator, whatsapp, alarm
from config import VOICE_ID, SPEECH_RATE, ALARM_FILE, NOTES_FILE, REMEMBER_FILE, EMAIL_USER, EMAIL_PASS, APP_MAPPINGS, WEBSITE_MAPPINGS

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[VOICE_ID].id)
engine.setProperty("rate", SPEECH_RATE)

# Initialize NLP
nlp = spacy.load("en_core_web_sm")

def speak(text: str) -> None:
    """Speak the provided text using the text-to-speech engine."""
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logger.error(f"Speech error: {e}")

def take_command() -> str:
    """Capture voice input and convert to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        logger.info("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.1)
        r.energy_threshold = 300
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=4)
            logger.info("Recognizing...")
            query = r.recognize_google(audio, language="en-in").lower()
            logger.info(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            logger.warning("No speech detected.")
            return "none"
        except sr.UnknownValueError:
            logger.warning("Could not understand audio.")
            return "none"
        except Exception as e:
            logger.error(f"Recognition error: {e}")
            return "none"

def wish_user() -> None:
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    greetings = {
        (0, 12): "Good Morning",
        (12, 18): "Good Afternoon",
        (18, 24): "Good Evening"
    }
    greeting = next(g for h, g in greetings.items() if h[0] <= hour < h[1])
    speak(f"{greeting} Sir! I am your Assistant, OWN 1.0.")

def get_username() -> str:
    """Prompt for and return the user's name."""
    speak("What should I call you, sir?")
    uname = take_command()
    if uname != "none":
        speak(f"Welcome, Mister {uname}")
        print(f"{'#'*20}\nWelcome Mr. {uname}\n{'#'*20}".center(shutil.get_terminal_size().columns))
        return uname
    return "User"

def send_email(to: str, content: str) -> bool:
    """Send an email to the specified recipient."""
    try:
        import smtplib
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to, content)
        server.close()
        return True
    except Exception as e:
        logger.error(f"Email error: {e}")
        return False

def process_command(query: str, username: str) -> bool:
    """Process the user's voice command."""
    doc = nlp(query)
    intent = "unknown"
    for token in doc:
        if token.lemma_ in ["open", "launch"]:
            intent = "open"
        elif token.lemma_ in ["close", "exit"]:
            intent = "close"
        elif token.lemma_ in ["search", "find"]:
            intent = "search"
        elif token.lemma_ in ["play", "music", "song"]:
            intent = "play"
        elif token.lemma_ in ["email", "mail"]:
            intent = "email"
        elif token.lemma_ in ["joke", "funny"]:
            intent = "joke"

    if intent == "open" or "open" in query:
        # Handle both apps and websites
        for app in APP_MAPPINGS:
            if app in query:
                apps.open_app(query)
                return True
        for site in WEBSITE_MAPPINGS:
            if site in query:
                apps.open_app(query)
                return True
    elif intent == "close" or "close" in query:
        apps.close_app(query)
        return True
    elif intent == "search" or any(x in query for x in ["google", "youtube", "wikipedia", "what is", "who is"]):
        search.search_query(query)
        return True
    elif intent == "play" or "play song" in query:
        music_dir = Path("C:/Users/Rohan S Mistry/Music")
        songs = list(music_dir.glob("*.mp3"))
        if songs:
            os.startfile(songs[0])
            speak("Playing music.")
        else:
            speak("No music files found.")
        return True
    elif intent == "email" or "email" in query:
        speak("What should I say?")
        content = take_command()
        if "mama" in query:
            to = "pritesh_02@yahoo.com"
        else:
            speak("To whom should I send the email?")
            to = take_command().replace(" ", "")
        if send_email(to, content):
            speak("Email sent successfully.")
        else:
            speak("Failed to send email.")
        return True
    elif intent == "joke" or "joke" in query:
        import pyjokes
        speak(pyjokes.get_joke())
        return True
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return True
    elif "exit" in query:
        speak(f"Goodbye, {username}. Thanks for using OWN 1.0.")
        return False
    elif "note" in query:
        if "write" in query:
            speak("What should I write?")
            note = take_command()
            with NOTES_FILE.open("a") as f:
                f.write(f"{datetime.datetime.now().strftime('%I:%M %p')}: {note}\n")
            speak("Note saved.")
        elif "show" in query:
            with NOTES_FILE.open("r") as f:
                content = f.read()
                print(content)
                speak(content[:100])  # Read first 100 chars
        return True
    elif "remember" in query:
        if "what do you remember" in query:
            with REMEMBER_FILE.open("r") as f:
                speak(f"You told me to remember: {f.read()}")
        else:
            message = query.replace("remember that", "").strip()
            with REMEMBER_FILE.open("a") as f:
                f.write(f"{message}\n")
            speak(f"I'll remember: {message}")
        return True
    elif "alarm" in query:
        speak("Please tell the time for the alarm (e.g., 10 and 30)")
        time_input = take_command().replace(" and ", ":")
        alarm.set_alarm(time_input)
        return True
    elif "news" in query:
        news.get_latest_news()
        return True
    elif "whatsapp" in query:
        whatsapp.send_whatsapp_message()
        return True
    elif "calculate" in query:
        calculator.calculate(query)
        return True
    elif any(cmd in query for cmd in ["select all", "copy", "cut", "paste", "pause", "resume", "forward", "backward", "change window"]):
        chrome_shortcut.handle_shortcut(query)
        return True
    elif "volume up" in query:
        keyboard.volume_up()
        return True
    elif "volume down" in query:
        keyboard.volume_down()
        return True
    else:
        speak("Sorry, I didn't understand that command.")
        return True

def main():
    """Main function to run the voice assistant."""
    wish_user()
    username = get_username()
    speak("How can I help you, sir?")
    
    while True:
        query = take_command()
        if query == "none":
            continue
        if not process_command(query, username):
            break

if __name__ == "__main__":
    main()