import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project directories
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# API keys (load from environment variables)
WOLFRAM_ALPHA_KEY = os.getenv("WOLFRAM_ALPHA_KEY", "3WR2KP-4U9X329R9U")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "1a1ac9b8505341478289bc11a04eb056")
EMAIL_USER = os.getenv("EMAIL_USER", "userid@gmail.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "your_password")

# Voice settings
VOICE_ID = 0
SPEECH_RATE = 170

# File paths
ALARM_FILE = DATA_DIR / "alarm.txt"
NOTES_FILE = DATA_DIR / "notes.txt"
REMEMBER_FILE = DATA_DIR / "remember.txt"

# Application mappings
APP_MAPPINGS = {
    "commandprompt": "cmd",
    "paint": "paint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "youtube music": r"C:\Users\Rohan S Mistry\AppData\Local\Programs\youtube-music-desktop-app\YouTube Music Desktop App.exe",
    "vs code": r"C:\Users\Rohan S Mistry\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}

# Website mappings
WEBSITE_MAPPINGS = {
    "google": "google.com",
    "youtube": "youtube.com",
    "facebook": "facebook.com",
    "twitter": "twitter.com",
    "wikipedia": "wikipedia.com",
    "instagram": "instagram.com",
    "baidu": "baidu.com",
    "yahoo": "yahoo.com",
    "yandex": "yandex.ru",
    "whatsapp": "whatsapp.com",
    "amazon": "amazon.com",
    "zoom": "zoom.us",
    "live": "live.com",
    "netflix": "netflix.com",
    "yahoo japan": "yahoo.co.jp",
    "vk": "vk.com",
    "reddit": "reddit.com",
    "office": "office.com",
    "naver": "naver.com",
    "pinterest": "pinterest.com",
    "discord": "discord.com",
    "linkedin": "linkedin.com",
    "cnn": "cnn.com",
    "microsoft": "microsoft.com",
    "mail": "mail.ru",
    "globo": "globo.com",
    "bing": "bing.com",
    "twitch": "twitch.tv",
    "google brazil": "google.com.br",
    "qq": "qq.com",
    "microsoft online": "microsoftonline.com",
    "ebay": "ebay.com",
    "msn": "msn.com",
    "yahoo news japan": "news.yahoo.co.jp",
    "duckduckgo": "duckduckgo.com",
    "ok": "ok.ru",
    "walmart": "walmart.com",
    "bilibili": "bilibili.com",
    "tiktok": "tiktok.com",
    "paypal": "paypal.com",
    "google germany": "google.de",
    "amazon japan": "amazon.co.jp",
    "aliexpress": "aliexpress.com",
    "amazon germany": "amazon.de",
    "rakuten japan": "rakuten.co.jp",
    "amazon uk": "amazon.co.uk"
}

def speak(text: str) -> None:
    """Speak the provided text using the text-to-speech engine."""
    import pyttsx3
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[VOICE_ID].id)
    engine.setProperty("rate", SPEECH_RATE)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        import logging
        logging.error(f"Speech error: {e}")