# lucy/skills/launcher.py
import os, subprocess, webbrowser
from lucy.io.speaker import speak

def handle_launch(command: str, cfg):
    """Launch apps or websites from config.yaml"""
    sites = cfg.get("sites", {})
    apps = cfg.get("apps", {})

    # Websites first
    for name, url in sites.items():
        if name in command:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return

    # Local apps
    for name, path in apps.items():
        if name in command:
            speak(f"Opening {name}")
            try:
                if path.endswith(".lnk") or path.endswith(".exe"):
                    subprocess.Popen(path, shell=True)
                else:
                    os.startfile(path)
            except Exception as e:
                speak(f"Sorry, I couldn’t open {name}.")
                print(f"❌ Error opening {name}: {e}")
            return

    speak("Sorry, I couldn’t find that app or site.")
