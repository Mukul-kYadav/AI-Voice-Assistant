import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
import requests
from functions.os_ops import open_camera, open_calculator, open_notepad, open_cmd
from functions.online_ops import my_ip, wiki, yt, google_search, whatsapp, send_mail, news, weather, joke


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# greet according to time 
def greet():
    hour = datetime.now().hour
    if(hour>=6)and(hour<12):
        speak(f"Good morning {USERNAME}")
    elif(hour>=12)and(hour<16):
        speak(f"Good afternoon {USERNAME}")
    elif(hour>=16)and(hour<19):
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour>=21 and hour<6:
                speak('Good Night sir, Take care!')
            else:
                speak("have a good day sir!")
            exit()
    except Exception:
        speak("Sorry, I could not understand. Could you please say that again?")
        query = None
    return query


if __name__ == "__main__":
    greet()
    while True:
        query = user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open calculator' in query:
            open_calculator()

        elif 'open camera' in query:
            open_camera()

        elif 'open cmd' in query or 'open command prompt' in query:
            open_cmd()
        
        elif 'ip address' in query:
            ip = my_ip()
            speak(f"Your IP address is {ip}. I am also printing it on the screen.")
            print(f"Your IP address is {ip}.")

        elif 'wikipedia' in query:
            speak("What do you want to search on wikipedia, sir?")
            search_query = user_input().lower()
            results = wiki(search_query)
            speak(f"According to wikipedia {results}")
            speak("You can also read it from the screen, sir!")
            print(results)

        elif 'youtube' in query:
            speak("what do you want to play on youtube, sir?")
            inp = user_input().lower()
            yt(inp)

        elif 'search on goole' in query or 'google search' in query:
            speak("What do you want to search on google, sir?")
            query = user_input().lower()
            google_search(query)

        elif 'whatsapp' in query:
            speak("sir, please enter the phone number in the console on which you want to send the messsage.")
            number = int(input("Enter number: "))
            speak("What is the message, sir?")
            message = user_input().lower()
            whatsapp(number, message)
            speak('message sent sir')

        elif 'email' in query:
            speak("Plese Enter Email id in the console sir")
            email = input("Emter email id: ")
            speak("What should be the subject sir?")
            sub = user_input().capitalize()
            speak("What is the message sir?")
            mess = user_input().capitalize()
            if send_mail(email, sub, mess):
                speak("I have sent the mail sir.")
            else:
                speak("I am sorry sir!, Something went wrong.")

        elif 'joke' in query:
            speak("I hope you like this one sir.")
            haha = joke()
            speak(haha)

        elif 'weather' in query:
            ip_address = my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = weather(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'news' in query:
            speak("The latest news headlines are")
            speak(news())
