import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("friday at your service please tell me How may i help you!")

def takeCommand():
    #it takes microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\VS CODE\FRIDAY_AI\ss\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishMe()
    while 1:
       query = takeCommand().lower()

       #logic for executing tasks based on query
       if 'wikipedia' in query:
            speak('Serching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

       elif "go offline" in query:
           speak("going offline")
           quit()

       elif "search in chrome" in query:
           speak("what should i search?")
           chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
           search = takeCommand().lower()
           wb.get(chromepath).open_new_tab(search + ".com")

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir, the time is {strTime}")

       elif 'open code' in query:
           codePath = "C:\\Users\\A\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
        
       elif "log out" in query:
           os.system("shutdown -l")

       elif "shutdown" in query:
           os.system("shutdown /s /t 1")

       elif "restart" in query:
           os.system("shutdown /r /t 1")
       
       elif "remember that" in query:
           speak("what should i remember?")
           data = takeCommand()
           speak("you said me to remember" + data)
           remember = open("data.txt", "w")
           remember.write(data)
           remember.close()

       elif "do you know anything" in query:
           remember = open("data.txt","r")
           speak("you said me to remember that"+ remember.read())
       
       elif "screenshot" in query:
            screenshot()
            speak("done") 
    
       elif "cpu" in query:
              cpu()
        
       elif "joke" in query:
           jokes()