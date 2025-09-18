import pyjokes
import random
from lucy.io.speaker import speak

# Some static facts & quotes
facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old.",
    "Bananas are berries, but strawberries are not.",
    "Octopuses have three hearts.",
    "A day on Venus is longer than a year on Venus.",
]

quotes = [
    "The best way to predict the future is to invent it.",
    "In the middle of every difficulty lies opportunity. — Albert Einstein",
    "Do what you can, with what you have, where you are. — Theodore Roosevelt",
    "Happiness is not something ready made. It comes from your own actions. — Dalai Lama",
]


def tell_joke_or_fact(command: str):
    """
    Handle jokes, facts, and quotes.
    """
    command = command.lower()

    if "joke" in command:
        joke = pyjokes.get_joke()
        print("Joke:", joke)
        speak(joke)
        return

    if "fact" in command:
        fact = random.choice(facts)
        print("Fact:", fact)
        speak(fact)
        return

    if "quote" in command:
        quote = random.choice(quotes)
        print("Quote:", quote)
        speak(quote)
        return

    speak("Sorry, I don’t know that one.")
