import requests
import json
from config import speak, NEWS_API_KEY

def get_latest_news() -> None:
    """Fetch and read the latest news."""
    api_urls = {
        "business": f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={NEWS_API_KEY}",
        "entertainment": f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={NEWS_API_KEY}",
        "health": f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={NEWS_API_KEY}",
        "science": f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={NEWS_API_KEY}",
        "sports": f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={NEWS_API_KEY}",
        "technology": f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={NEWS_API_KEY}"
    }
    speak("Which news category? Business, health, technology, sports, entertainment, or science?")
    category = input("Type the category: ").lower()
    url = api_urls.get(category)
    if not url:
        speak("Invalid category.")
        return

    try:
        response = requests.get(url)
        news = json.loads(response.text)
        speak("Here are the latest headlines.")
        for article in news["articles"][:3]:  # Limit to 3 articles
            title = article["title"]
            print(title)
            speak(title)
            print(f"More info: {article['url']}")
            if input("Continue? (y/n): ").lower() != "y":
                break
        speak("That's all for now.")
    except Exception as e:
        speak("Failed to fetch news.")
        print(e)