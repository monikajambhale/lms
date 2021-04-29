import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#sapi5 is used to take voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Zaris. How may I help you?")

#Takes speech input from the user and returns string output
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1     #While speaking, if you take a pause, it will not consider your command to be complete
        audio=r.listen(source)
    
    try:
        print("Recognizing your command..")
        query=r.recognize_google(audio,language='en-in')
        print("You said: "+query,"\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('monikajambhale7@gmail.com','70021017139')
    server.sendmail('monikajambhale7@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    if 1:
    # while(True):
        query=takeCommand().lower()     #Logic to execute tasks based on the command
        if 'wikipedia' in query:
            speak("Searching wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia, ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open amzon prime' in query:
            webbrowser.open("primevideo.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("Ma'am, the time is ",strTime)

        elif 'open code' in query:
            codepath="C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)

        elif 'email to myself' in query:
            try:
                spreak("What should I say?")
                content=takeCommand()
                to="monikajambhale7@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")
