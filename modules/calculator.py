import wolframalpha
from config import speak, WOLFRAM_ALPHA_KEY

def calculate(query: str) -> None:
    """Perform mathematical calculations using Wolfram Alpha."""
    query = query.replace("calculate", "").replace("jarvis", "").strip()
    query = query.replace("multiply", "*").replace("plus", "+").replace("minus", "-").replace("divide", "/")
    try:
        client = wolframalpha.Client(WOLFRAM_ALPHA_KEY)
        result = next(client.query(query).results).text
        speak(f"The answer is {result}")
        print(result)
    except:
        speak("Sorry, I couldn't calculate that.")