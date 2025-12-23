import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import requests
from openai import OpenAI

# ================= CONFIG ================= #
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
STABLE_DIFFUSION_API = "YOUR_STABLE_DIFFUSION_API_KEY"

client = OpenAI(api_key=OPENAI_API_KEY)

# ================= INIT ================= #
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id if len(voices) > 1 else voices[0].id)
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

# ================= SPEAK ================= #
def speak(text):
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

# ================= LISTEN ================= #
def listen():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=0.5)
            print("🎤 Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print("User:", command)
            return command
    except sr.UnknownValueError:
        speak("I did not understand, please repeat.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# ================= CHAT AI ================= #
def chat_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "AI service is currently unavailable."

# ================= IMAGE GENERATION ================= #
def generate_image(prompt):
    speak("Generating image")
    payload = {
        "prompt": prompt,
        "steps": 30
    }
    try:
        response = requests.post(
            "https://stablediffusionapi.com/api/v3/text2img",
            json=payload,
            headers={"Authorization": STABLE_DIFFUSION_API}
        )
        image_url = response.json()["output"][0]
        speak("Image generated")
        os.system(f"start {image_url}")
    except:
        speak("Failed to generate image.")

# ================= APP CONTROL ================= #
def open_app(app):
    os.system(f"start {app}")

# ================= PROCESS COMMAND ================= #
def process_command(command):
    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Current time is {time}")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, 2)
            speak(info)
        except:
            speak(f"I could not find information about {person}")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "open" in command:
        app = command.replace("open", "").strip()
        speak(f"Opening {app}")
        open_app(app)

    elif "generate image" in command:
        prompt = command.replace("generate image", "").strip()
        generate_image(prompt)

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        sys.exit()

    else:
        reply = chat_ai(command)
        speak(reply)

# ================= MAIN LOOP ================= #
speak("Advanced AI Assistant Activated")

try:
    while True:
        cmd = listen()
        if cmd:
            process_command(cmd)
except KeyboardInterrupt:
    speak("Assistant stopped safely")
    sys.exit()
