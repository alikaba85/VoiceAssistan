import pyttsx3  #pip ile yüklüyor import ediyoruz
import datetime #zaman işleci
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import googletrans
import nltk
import requests
import pywhatkit
import clipboard
import newsapi
from pip._internal.cli.cmdoptions import python




sesli = pyttsx3.init()


def talk(audio):
    sesli.say(audio)
    sesli.runAndWait()

talk("Hi I Am Colly")

def time():
    Time = datetime.datetime.now().strftime("%I: %M: %S")
    talk(Time)

def date():
    years = int(datetime.datetime.now().year)
    mount = int(datetime.datetime.now().month)
    days = int(datetime.datetime.now().day)
    talk(years)
    talk(mount)
    talk(days)

def dinle():
    talk("Welcome")
    talk("The time is now ")
    time()
    talk("date is now")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        talk("Good Morning")
    elif hour >= 12 and hour<18:
        talk("Good Afternoon")
    elif hour >= 18 and hour <24:
        talk("Good Evening")
    else:
        talk("Good Night")
    talk("what is the topic?")



def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        say = r.recognize_google(audio,language="en")
        print(say)

    except Exception as e:
        print(e)
        print("Again Say")
        return None
    return say


def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('asd9@gmail.com', 'Bme345')
        server.sendmail('sss5@gmail.com', to, content)
        server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\MYPROJECT\\Pythoon\\VoiceAssistan\\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    talk("Cpu is at"+usage)
    battery = psutil.sensors_battery()
    talk("Battery is at")
    talk(battery.percent)



def jokes():
    talk(pyjokes.get_joke())




def main():
    dinle()
    while True:
        say = Command()
        if 'time' in say:
            time()
        elif 'date' in say:
            date()
        elif 'wikipedia' in say:
            talk("Searching...")
            say = say.replace("wikipedia")
            result = wikipedia.summary(say, sentences=2)
            print(result)
            talk(result)

        elif 'send email' in say:
            try:
                talk("What Should I Say")
                content = Command().lower
                to = 'akaba2095@gmail.com'
                sendEmail(to, content)
                talk("Email Sent")
            except Exception as e:
                print(e)
                talk("Email not sent")

        elif 'search in chrome' in say:
            talk("What Should I Say")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = Command()
            wb.get(chromepath).open_new_tab(search + '.com')


        elif 'logout' in say:
            os.system('Shutdown -l')

        elif 'shutdown' in say:
            os.system('Shutdown /s /t l')

        elif 'restart' in say:
            os.system('shutdown /r /t l')

        elif 'play songs' in say:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in say:
            talk("What Should I Say")
            data = Command().lower
            talk("You said to me remember " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in say:
            remember = open('data.txt', 'r')
            talk("You said to me remember that " + remember.read())

        elif 'screenshot' in say:
            screenshot()
            talk("Done")

        elif 'CPU' in say:
            cpu()

        elif 'walk' in say:
            jokes()




        elif 'offline' in say:
            quit()


if __name__ == "__main__":
    main()



