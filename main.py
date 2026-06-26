import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize OpenAI client — add your API key here
client = OpenAI(
    api_key="Your_API_Key_Here",
)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Alex skilled in general tasks like Alexa and Google Cloud. Give short and concise answers."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if  "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif  "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif  "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        print(song)
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        # If command is not recognized, let AI handle it
        output = aiProcess(c)
        speak(output)
        



if __name__ == "__main__":
    speak("Initializing Alex....")
    while True:
        #Listen for the wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()


        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=1,phrase_time_limit=2)
            print("Recognizing....")
            word = r.recognize_google(audio)
            if (word.lower() == "hello"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Alex active...")
                    audio = r.listen(source,timeout=3,phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    # print(command)

                    processCommand(command)
                    
            
        except Exception as e:
            print("Error; {0}".format(e))
