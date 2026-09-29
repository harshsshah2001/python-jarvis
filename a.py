import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import subprocess
import urllib.parse
import time


# =========================
# INITIALIZATION
# =========================

recognizer = sr.Recognizer()

# Make speech recognition faster
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.6

engine = pyttsx3.init()

# Speech speed
engine.setProperty("rate", 180)

# Volume
engine.setProperty("volume", 1.0)


# =========================
# SPEAK FUNCTION
# =========================

def speak(text):
    print("Jarvis:", text)

    engine.say(text)
    engine.runAndWait()


# =========================
# LISTEN FUNCTION
# =========================

def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        # Adjust only once for a short time
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

    try:

        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You:", query)

        return query.lower()

    except sr.UnknownValueError:

        print("Sorry, I didn't understand.")

        return ""

    except sr.RequestError:

        speak("Speech recognition service is unavailable.")

        return ""


# =========================
# OPEN WEBSITE
# =========================

def open_website(url, message):

    speak(message)

    webbrowser.open(url)


# =========================
# GOOGLE SEARCH
# =========================

def google_search(query):

    search_query = query.replace("search", "").strip()

    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(search_query)
    )

    speak("Searching Google.")

    webbrowser.open(url)


# =========================
# YOUTUBE SEARCH
# =========================

def youtube_search(query):

    search_query = query.replace("youtube", "").strip()

    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(search_query)
    )

    speak("Opening YouTube.")

    webbrowser.open(url)


# =========================
# TIME
# =========================

def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"The time is {current_time}")


# =========================
# DATE
# =========================

def tell_date():

    today = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    speak(f"Today is {today}")


# =========================
# OPEN APPLICATION
# =========================

def open_application(app):

    apps = {

        "notepad": "notepad.exe",

        "calculator": "calc.exe",

        "paint": "mspaint.exe",

        "command prompt": "cmd.exe",

    }

    if app in apps:

        speak(f"Opening {app}.")

        subprocess.Popen(apps[app])

    else:

        speak("I don't know that application.")


# =========================
# PROCESS COMMAND
# =========================

def process_command(query):

    if not query:
        return True


    # -------------------------
    # GREETING
    # -------------------------

    if "hello" in query or "hi" in query:

        speak("Hello Harsh. How can I help you?")

        return True


    # -------------------------
    # HOW ARE YOU
    # -------------------------

    if "how are you" in query:

        speak("I am doing great. Ready to help you.")

        return True


    # -------------------------
    # TIME
    # -------------------------

    if "what time" in query or "current time" in query:

        tell_time()

        return True


    # -------------------------
    # DATE
    # -------------------------

    if "what date" in query or "today's date" in query:

        tell_date()

        return True


    # -------------------------
    # YOUTUBE
    # -------------------------

    if query.startswith("youtube"):

        youtube_search(query)

        return True


    if "open youtube" in query:

        open_website(
            "https://www.youtube.com",
            "Opening YouTube."
        )

        return True


    # -------------------------
    # GOOGLE
    # -------------------------

    if query.startswith("search"):

        google_search(query)

        return True


    if "open google" in query:

        open_website(
            "https://www.google.com",
            "Opening Google."
        )

        return True


    # -------------------------
    # GITHUB
    # -------------------------

    if "open github" in query:

        open_website(
            "https://github.com",
            "Opening GitHub."
        )

        return True


    # -------------------------
    # CHATGPT
    # -------------------------

    if "open chatgpt" in query:

        open_website(
            "https://chatgpt.com",
            "Opening ChatGPT."
        )

        return True


    # -------------------------
    # WHATSAPP WEB
    # -------------------------

    if "open whatsapp" in query:

        open_website(
            "https://web.whatsapp.com",
            "Opening WhatsApp."
        )

        return True


    # -------------------------
    # INSTAGRAM
    # -------------------------

    if "open instagram" in query:

        open_website(
            "https://www.instagram.com",
            "Opening Instagram."
        )

        return True


    # -------------------------
    # NOTEPAD
    # -------------------------

    if "open notepad" in query:

        open_application("notepad")

        return True


    # -------------------------
    # CALCULATOR
    # -------------------------

    if "open calculator" in query:

        open_application("calculator")

        return True


    # -------------------------
    # PAINT
    # -------------------------

    if "open paint" in query:

        open_application("paint")

        return True


    # -------------------------
    # COMMAND PROMPT
    # -------------------------

    if "open command prompt" in query:

        open_application("command prompt")

        return True


    # -------------------------
    # EXIT
    # -------------------------

    if (
        "exit" in query
        or "quit" in query
        or "goodbye" in query
        or "stop jarvis" in query
    ):

        speak("Goodbye Harsh. Have a great day.")

        return False


    # -------------------------
    # UNKNOWN COMMAND
    # -------------------------

    speak(
        "I don't know that command yet."
    )

    return True


# =========================
# MAIN
# =========================

def main():

    speak("Jarvis is online.")

    speak("How can I help you?")

    while True:

        query = listen()

        if not process_command(query):

            break

        # Small delay prevents microphone
        # from immediately picking up Jarvis voice
        time.sleep(0.2)


# =========================
# START
# =========================

if __name__ == "__main__":

    main()