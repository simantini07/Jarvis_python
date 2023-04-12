import pyttsx3
import speech_recognition as sr
from datetime import datetime    #To provide current or live time to A.I.
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe():
    hour = int(datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("I am Jarvis Mam, How may I help you")
def takeCommand():                                #return a string output by taking microphone input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   
                           #while talking if I take a pause it should not consider it a completed sentnce
        audio = r.listen(source)                   #from speech recog Module
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:  {query}\n")
    except Exception as error:
        print(error)

        print("Say that again please...")
        return "None"                               #It will return a None string if there is any problem.
    return query
#def sendEmail(to, content):



if __name__ == "__main__":   #This function is for the Jarvis to speak 
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)  #It will read two sentences from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)   #Whatever you have searched, speak it
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'open spotify' in query:
            webbrowser.open("https://spotify.com")
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is: {strTime}")
        '''elif 'email to simantini' in query:
            try:
                speak("What should I say??")
                content = takeCommand()
                to = "simantinir07@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as error:
                print(error)

                print("Sorry bhai, I couldnt send the email")'''


