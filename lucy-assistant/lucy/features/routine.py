import requests
from datetime import datetime
from lucy.io.speaker import speak


def handle_routine(cfg):
    """
    Responds to 'good morning' by telling the time, weather, and news headlines.
    """

    # Greet
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning!"
    elif hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"

    speak(f"{greeting} Here's your daily briefing.")

    # Time
    now_time = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now_time}")

    # Weather
    weather_key = cfg["apis"]["openweather"]["key"]
    city = cfg["apis"]["openweather"]["city"]
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"

    try:
        response = requests.get(weather_url).json()
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        speak(f"The current temperature in {city} is {temp}°C with {desc}.")
    except Exception:
        speak("Sorry, I could not fetch the weather right now.")

    # News
    news_key = cfg["apis"]["newsapi"]["key"]
    news_url = f"https://newsapi.org/v2/top-headlines?country={cfg['apis']['newsapi']['country']}&apiKey={news_key}"

    try:
        articles = requests.get(news_url).json().get("articles", [])
        if articles:
            speak("Here are the top news headlines.")
            for article in articles[:3]:  # limit to 3 headlines
                speak(article["title"])
        else:
            speak("I couldn’t find any news headlines right now.")
    except Exception:
        speak("Sorry, I couldn’t fetch the news at the moment.")
