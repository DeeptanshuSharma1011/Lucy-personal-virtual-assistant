# lucy/features/translator.py

from googletrans import Translator
from lucy.io.speaker import speak

def handle_translation(command, cfg):
    """
    Translate phrases like:
    - 'translate good morning in spanish'
    - 'translate hello in french'
    """

    translator = Translator()

    try:
        # Example command: "translate good morning in spanish"
        parts = command.split("translate")[-1].strip()

        if " in " in parts:
            phrase, lang = parts.rsplit(" in ", 1)
            phrase, lang = phrase.strip(), lang.strip()
        else:
            # If no language is given, fallback to config or default Hindi
            phrase, lang = parts, cfg.get("default_lang", "hindi")

        # Do the translation
        result = translator.translate(phrase, dest=lang)
        translation = result.text

        # Speak and show result
        speak(f"{phrase} in {lang} is {translation}")
        print(f"✅ Translation: {phrase} → {translation} ({lang})")

    except Exception as e:
        speak("Sorry, I couldn’t translate that.")
        print(f"❌ Translation error: {e}")
