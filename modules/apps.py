import os
import pyautogui
import webbrowser
from time import sleep
from config import speak, APP_MAPPINGS, WEBSITE_MAPPINGS
import logging

logger = logging.getLogger(__name__)

def open_app(query: str) -> None:
    """Open an application or website."""
    speak("Launching...")
    query = query.lower().replace("open", "").replace("hey", "").strip()
    
    # Check for website
    for site, url in WEBSITE_MAPPINGS.items():
        if site in query:
            webbrowser.open(f"https://{url}")
            speak(f"Opening {site}")
            return
    
    # Check for application
    for app, path in APP_MAPPINGS.items():
        if app in query:
            try:
                if path.endswith(".exe"):
                    os.startfile(path)
                else:
                    os.system(f"start {path}")
                speak(f"Opening {app}")
            except Exception as e:
                logger.error(f"Failed to open {app}: {e}")
                speak(f"Failed to open {app}")
            return
    
    # Fallback for generic website
    if any(x in query for x in [".com", ".co.in", ".org"]):
        webbrowser.open(f"https://www.{query}")
        speak(f"Opening {query}")
    else:
        speak("Application or website not recognized.")

def close_app(query: str) -> None:
    """Close an application or browser tabs."""
    speak("Closing...")
    query = query.lower()
    if "tab" in query:
        num_tabs = int(query.split("tab")[0].strip()) if query.split("tab")[0].strip().isdigit() else 1
        for _ in range(num_tabs):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("Tabs closed.")
    else:
        for app, path in APP_MAPPINGS.items():
            if app in query and not path.endswith(".exe"):
                try:
                    os.system(f"taskkill /f /im {path}.exe")
                    speak(f"Closed {app}")
                except Exception as e:
                    logger.error(f"Failed to close {app}: {e}")
                    speak(f"Failed to close {app}")
                return
        speak("Application not recognized.")