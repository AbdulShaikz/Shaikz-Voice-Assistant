import pyttsx3 #importing python text to speech module pip install pyttsx3 //another module is gtts which is google text to speech library
import datetime #importing date and time module
import speech_recognition as sr #importing speech regonition module pip install SpeechRecognition
import wikipedia #importing wikipedia module pip install wikipedia
import smtplib #mailing library
import webbrowser as wb #web browser library
import os #inbuilt os library
import pyautogui #screenshot
import psutil #pip install psutil
import pyjokes #python jokes library
import requests 
import json  #weather
import time

engine = pyttsx3.init()

#voices = engine.getProperty('voices')
#print(voices[1].id)
#engine.setProperty('voice',voices[0].id)

name=""

#User defined function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is :")
    speak(Time)
    
def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("Today's date is :")
    speak(day)
    speak(month)
    speak(year)
    
def greet():
    speak("As-salamu alaykum")
    speak("Welcome!I'm Shaikz assistant.") 
    
    if(os.stat("name.txt").st_size == 0):
        speak("how should I refer to you?") 
        name = takeCommand()
        name = name.replace("refer me as","")
        name = name.replace("call me as","")
        myName = open("myname.txt","w")
        myName.write(name)
        myName.close()
    myName = open("myname.txt","w+")
    speak("Well "+myName.read())
    speak("How can i help you?")
    
def myName():
    myName = open("myname.txt","r")
    speak("You said your name is"+myName.read())
def changeName():
    speak("Welcome!I'm Shaikz assistant.") 
    speak("how should I refer to you?") 
    name = takeCommand()
    name = name.replace("refer me as","")
    name = name.replace("call me as","")
    myName = open("myname.txt","w")
    myName.write(name)
    myName.close()
    speak("Your name has been updated.")

def bye():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Have a Good Morning!")
    elif hour>=12 and hour<=17:
        speak("Have a Good afternoon!")
    elif hour>=17 and hour<=21:
        speak("Have a Good evening!")
    else:
        speak("Good night")
    speak("bye...Take care, see you again")
    speak("ALLAH hafiz")
    quit()
    
def takeCommand():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        recognize.adjust_for_ambient_noise(source, duration = 0.8)
        #recognize.pause_threshold = 0.8
        audio = recognize.listen(source)
    try:
        print("Recognizing.....")
        query = recognize.recognize_google(audio,language='en-IN').lower()
        print(query)
        
    except Exception as e:
        print(e)
        speak("Can you please say it again..")
        query = takeCommand()
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587) #gmail port no.587
    server.ehlo()
    server.starttls()  #tls - transport layer security
    # server.login("email","xyz")
    # server.sendmail("email",to,content)
    server.close()

def takeSnap():
    img = pyautogui.screenshot()
    img.save("E:\\PyhtonProjects\\Shaikz Assistant Screenshots\\snap_1.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery = psutil.sensors_battery() 
    speak("Battery percentage is : ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ =="__main__":
    greet()
    while True:
        
        query  = takeCommand().lower()
        
        if "time" in query:
            time()
        
        elif "date" in query:
            date()
        
        elif "my name" in query:
            myName()
            
        elif "change my name" in query:
            changeName()
        
        elif "send email" in query:
            try:
                speak("Tell the mail id to whom i should send an email :")
                toEmail = 'shabaazstar@gmail.com'
                speak("What should i send,tell me the content")
                content = takeCommand()
                sendEmail(toEmail,content)
                speak("Email has been successfully delivered!")
            except Exception as e:
                print(e)
                speak("Unable to send the mail,Try again!")
        
        elif "wikipedia" in query:
            speak("Searching..")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        
        elif "logout" in query:
            os.system("shutdown -l")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "search in google" in query:
            speak("What would you like to search?")
            query = takeCommand()
            chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = query.replace("search in google","")
            wb.get(chromePath).open_new_tab(search)

        elif "open google" in query:
            speak("Opening google.....")
            chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            query = query.replace("open","")
            wb.get(chromePath).open_new_tab("google.com")

        elif "open youtube" in query:
            speak("Opening youtube.....")
            chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            query = query.replace("open","")
            wb.get(chromePath).open_new_tab("youtube.com")

        elif "open facebook" in query:
            speak("Opening facebook.....")
            chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            query = query.replace("open","")
            wb.get(chromePath).open_new_tab("facebook.com")
        
        elif "play songs" in query:
            songs_dir ="path"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif "screenshot" in query:
            takeSnap()
            speak("Done!")
        
        elif 'cpu' in query:
            cpu()
        
        elif "jokes" in query:
            jokes()
            time.sleep(3)
            
        elif "do you remember anything?" in query:
            remember = open("data.txt",'r')
            speak("You said me to remember "+remember.read())
        
        elif "remember" in query:
            speak("What should i remeber?")
            data = takeCommand()
            remember = open("data.txt",'w')
            remember.write(data)
            remember.close()
            speak("You said me to remember that"+remember.read())
            speak("Done!")

        elif "weather in" in query:
            city = query.split("in", 1)[1]   
            #openweathermap API
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b408e4289b126e6920673aed1cb12007&units=metric'.format(city) #api url
            response = requests.get(url.format(city))
            data = response.json()
            #print(data)
            temp = data['main']['temp']
            round_temp = int(round(temp))
            speak('It is {} degree celcius in {}'.format(round_temp, city))
            time.sleep(3)
            
        elif "bye"  or "offline" in query:
            bye()