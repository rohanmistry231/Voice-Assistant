import pywhatkit
from datetime import datetime, timedelta
from config import speak

def send_whatsapp_message() -> None:
    """Send a WhatsApp message."""
    speak("Who do you want to message?")
    recipient = input("Enter recipient number (e.g., +919925336945) or name (Person 1, Person 2): ")
    contacts = {
        "person 1": "+919925336945",
        "person 2": "+91xxxxxxxxxx"  # Add another contact
    }
    phone = contacts.get(recipient.lower(), recipient)
    speak("What's the message?")
    message = input("Enter the message: ")
    time_hour = int(datetime.now().strftime("%H"))
    time_min = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))
    try:
        pywhatkit.sendwhatmsg(phone, message, time_hour, time_min)
        speak("Message scheduled.")
    except Exception as e:
        speak("Failed to send message.")
        print(e)