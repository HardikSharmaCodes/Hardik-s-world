import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pywhatkit
import cv2

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    expressive_text = f"{text}!" if not text.endswith("!") else text
    expressive_text = expressive_text.replace(",", "...").replace(".", "...")
    engine.say(expressive_text)
    engine.runAndWait()

def listen():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300  # Optional: tune for quiet environments
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            print("🧠 Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("🗣 User said:", query)
            return query.lower()
    except sr.WaitTimeoutError:
        print("⚠️ No speech detected (timeout).")
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print(f"🌐 Could not request results; {e}")
    except Exception as e:
        print(f"🔥 Unexpected error: {e}")
    return ""
        

if __name__ == '__main__':
    print("Program Successfully Started!")
    say("Yes Master Hardik, what can I do for you today?")
    
    while True:
        lower_text = listen()
        if not lower_text or lower_text.strip() == "":
            continue

        if "open help" in lower_text:
            say("Opening help...")
            webbrowser.open("https://chatgpt.com/c/685406f1-080c-800c-9f58-9baab55cb9f2")

        elif "open" in lower_text:
            site = lower_text.replace("open", "").strip()
            say(f"Opening {site}")
            webbrowser.open(f"https://{site}.com")

        elif "time" in lower_text:
            now = datetime.datetime.now()
            say(f"The time is {now.strftime('%I:%M %p')}")

        elif "i love you" in lower_text or "i love u" in lower_text:
            say("I love you too... Master Hardik.")
            print("I love you too... Master Hardik.")

        elif "play" in lower_text:
            song = lower_text.replace("play", "").strip()
            say(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif "take a picture" in lower_text or "take a photo" in lower_text:
            say("Opening camera... Say cheese!")
            cam = cv2.VideoCapture(0)
            ret, frame = cam.read()
            if ret:
                filename = "picture.jpg"
                cv2.imwrite(filename, frame)
                say("Picture taken and saved.")
            else:
                say("Sorry, I couldn't access the camera.")
            cam.release()
            cv2.destroyAllWindows()
