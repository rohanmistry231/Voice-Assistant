import pyautogui
from config import speak

def handle_shortcut(query: str) -> None:
    """Handle keyboard shortcuts for browser actions."""
    shortcuts = {
        "select all": ("ctrl", "a"),
        "copy": ("ctrl", "c"),
        "cut": ("ctrl", "x"),
        "paste": ("ctrl", "v"),
        "pause": "space",
        "resume": "space",
        "forward": "right",
        "backward": "left",
        "change window": ("alt", "tab")
    }
    for cmd, keys in shortcuts.items():
        if cmd in query:
            if isinstance(keys, tuple):
                pyautogui.hotkey(*keys)
            else:
                pyautogui.press(keys)
            speak(f"{cmd.capitalize()} executed.")
            break