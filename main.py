import speech_recognition as sr
import pyttsx3
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text); engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        audio = r.listen(src)
    try:
        return r.recognize_google(audio).lower()
    except:
        speak("Sorry.")
        return ""

def open_app(pkg):
    os.system(f"am start -n {pkg}")
    speak("Opening app")

def action(cmd):
    if "hello chiru" in cmd: speak("Hello Sir")
    elif "open youtube" in cmd: open_app("com.google.android.youtube/.HomeActivity")
    elif "open chrome" in cmd: open_app("com.android.chrome/com.google.android.apps.chrome.Main")
    elif "open camera" in cmd: open_app("com.android.camera/.Camera")
    elif "open spotify" in cmd or "play music" in cmd: open_app("com.spotify.music/.MainActivity")
    elif "open contacts" in cmd: open_app("com.android.contacts/.DialtactsActivity")
    elif "open calculator" in cmd: open_app("com.android.calculator2/.Calculator")
    elif "open whatsapp" in cmd: open_app("com.whatsapp/.Main")
    elif "open instagram" in cmd: open_app("com.instagram.android/.activity.MainTabActivity")
    elif "search" in cmd:
        speak("What should I search?")
        q = listen()
        webbrowser.open(f"https://www.google.com/search?q={q}")
        speak(f"Searching {q}")
    elif "exit" in cmd:
        speak("Goodbye Sir"); exit()
    else:
        speak("Sorry, didn't get that.")

speak("Hello Sir. I am Chiru, your voice assistant.")
while True:
    c = listen()
    if c: action(c)
