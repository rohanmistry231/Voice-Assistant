import datetime
import os
from config import speak, ALARM_FILE

def set_alarm(time_str: str) -> None:
    """Set an alarm for the specified time."""
    with ALARM_FILE.open("a") as f:
        f.write(f"{time_str}\n")
    speak("Alarm set.")
    ring(time_str)

def ring(time_str: str) -> None:
    """Check and trigger the alarm."""
    alarm_time = time_str.replace(" and ", ":")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time.startswith(alarm_time):
            speak("Alarm ringing, sir!")
            os.startfile("music.mp3")  # Ensure music.mp3 exists
            break
        datetime.datetime.now().sleep(1)
    with ALARM_FILE.open("w") as f:
        f.write("")