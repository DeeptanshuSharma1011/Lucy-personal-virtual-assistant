import datetime
import requests
from lucy.io.speaker import speak

def get_weather(cfg):
    """Fetch current weather from OpenWeather API"""
    api_key = cfg["apis"]["openweather"]["key"]
    city = cfg["apis"]["openweather"]["city"]

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return "Weather data not available."

    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    return f"It's {temp}°C with {desc} in {city}."

def get_news(cfg):
    """Fetch latest headlines from NewsAPI"""
    api_key = cfg["apis"]["newsapi"]["key"]
    country = cfg["apis"]["newsapi"]["country"]

    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    response = requests.get(url).json()

    articles = response.get("articles", [])
    headlines = [a["title"] for a in articles[:5]]  # top 5 headlines

    return headlines if headlines else ["No news available."]

def daily_routine(cfg):
    """Perform Lucy's morning routine"""
    # Greeting with current time
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greet = "Good morning"
    elif hour < 18:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    speak(f"{greet}! The time is {now.strftime('%I:%M %p')}.")

    # Weather
    weather = get_weather(cfg)
    speak(weather)

    # News
    headlines = get_news(cfg)
    if headlines and len(headlines) > 0:
        speak("Here are the top news headlines.")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
            speak(headline)
    else:
        speak("Sorry, I couldn't fetch the news right now.")
