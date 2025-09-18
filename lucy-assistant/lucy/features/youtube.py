import webbrowser
from lucy.io.speaker import speak

def play_on_youtube(command: str):
    """Plays a song or video on YouTube based on voice command."""
    try:
        # Remove trigger words
        query = command.lower().replace("play", "").replace("on youtube", "").strip()

        if not query:
            speak("What would you like me to play on YouTube?")
            return

        url = f"https://www.youtube.com/results?search_query={query}"
        speak(f"Playing {query} on YouTube")
        webbrowser.open(url)

    except Exception as e:
        speak("Sorry, I couldn’t open YouTube right now.")
        print(f"[YouTube Error] {e}")
