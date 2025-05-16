from pynput.keyboard import Key, Controller
from time import sleep
from config import speak

keyboard = Controller()

def volume_up() -> None:
    """Increase system volume."""
    for _ in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
    speak("Volume increased.")

def volume_down() -> None:
    """Decrease system volume."""
    for _ in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
    speak("Volume decreased.")