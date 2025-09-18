import wikipedia
import webbrowser
from lucy.io.speaker import speak

def handle_search(command: str):
    """Handle Wikipedia or Google search based on user command"""
    try:
        if "wikipedia" in command:
            topic = command.replace("search", "").replace("wikipedia", "").strip()
            if topic:
                speak(f"Searching Wikipedia for {topic}")
                summary = wikipedia.summary(topic, sentences=2)
                print("Wikipedia:", summary)
                speak(summary)
            else:
                speak("What should I search on Wikipedia?")
        
        else:
            # Default: Google Search
            query = command.replace("search", "").strip()
            if query:
                speak(f"Searching Google for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("What should I search on Google?")
    
    except Exception as e:
        print("Search error:", e)
        speak("Sorry, I couldn’t complete the search.")
