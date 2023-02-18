import requests
import wikipedia 
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
NEWS_NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

# to get ip adderess
def my_ip():
    ip = requests.get('https://api64.ipify.org/?format=json')
    return ip["ip"]

# to add search on wikipedia
def wiki():
    result = wikipedia.summary(query, sentences = 2)
    return result

# to play o youtube
def yt(video):
    kit.playonyt(video)

# search on google 
def google_search(query):
    kit.search(query)

# send whatsapp message
def whatsapp(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

#to send Email


def send_mail(receiver_add, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject']  = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
    

# getting latest news
def news():
    headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        headlines.append(article["title"])
    return headlines[:5]

# getting weather report
def weather(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

# get random jokes
def joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

# 