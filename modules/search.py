import pywhatkit
import wikipedia
import webbrowser
from config import speak
import logging

logger = logging.getLogger(__name__)

def search_query(query: str) -> None:
    """Handle search queries for Google, YouTube, or Wikipedia."""
    query = query.lower().strip()
    
    if "google" in query:
        query = query.replace("google search", "").replace("google", "").strip()
        speak("Searching Google...")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=1, auto_suggest=False)
            speak(result)
        except Exception as e:
            logger.error(f"Google search error: {e}")
            speak("No additional information available.")
    
    elif "youtube" in query:
        query = query.replace("youtube search", "").replace("youtube", "").strip()
        speak("Searching YouTube...")
        try:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            pywhatkit.playonyt(query)
        except Exception as e:
            logger.error(f"YouTube search error: {e}")
            speak("Failed to search YouTube.")
    
    elif "wikipedia" in query or "what is" in query or "who is" in query:
        query = query.replace("wikipedia", "").replace("search wikipedia", "").replace("what is", "").replace("who is", "").strip()
        speak("Searching Wikipedia...")
        try:
            results = wikipedia.summary(query, sentences=2, auto_suggest=False)
            print(results)
            speak(results)
        except Exception as e:
            logger.error(f"Wikipedia search error: {e}")
            speak("No results found on Wikipedia.")