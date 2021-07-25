import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm = "******8@gmail.com"
pwd="*******"

r=sr.Recognizer()

engine = pyttsx3.init()  #Defining an engine for text to speech
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(str):          #function for text to speech
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str= "Sorry could not recognize what you said"
            speak(str)

def sendmail():
    rec = "***********@gmail.com"

    str = "Please speak body of mail"
    speak(str)
    msg=listen()

    str= "You have spoken the message"
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(unm, pwd)
    server.sendmail(unm,rec,msg)
    server.quit()

    str="The email has been sent"
    speak(str)

def readmail():

    server=e.connect("imap.gmail.com",unm,pwd)
    server.listids()

    str="Please say the serial no of email you wanna read starting from latest"
    speak(str)

    a=listen()
    if(a=="Tu"):
        a="2"

    b=int(a) - 1

    email=server.mail(server.listids()[b])

    str="The email is from:"
    speak(str)
    speak(email.from_addr)
    str="The subject of email is:"
    speak(str)
    speak(email.title)
    str="The body of email is:"
    speak(str)
    speak(email.body)

str = "Welcome to voice controlled email service"
speak(str)

while(1):
    str="What do you want to do?"
    speak(str)

    str="Speak SEND to send email    Speak READ to read inbox        Speak EXIT to exit"
    speak(str)

    ch=listen()
    if(ch == 'send') :
        str="You have chosen to send email"
        speak(str)
        sendmail()

    elif(ch == 'read'):
        str="You have chosen to read email"
        speak(str)
        readmail()

    elif(ch=='exit'):
        str="You have chosen to exit"
        speak(str)
        exit(1)

    else:
        str="Invalid choice:"
        speak(str)
        speak(ch)
