import pyttsx3 #python text to speech
import datetime #current data
import speech_recognition as sr 
import wikipedia 
import webbrowser 
import os
from googlesearch import search #pip install googlesearch-python
import random 
import pywhatkit
from gnewsclient import gnewsclient #pip install gnewsclient
import wolframalpha #pip install wolframalpha
import time as timee
import smtplib
from email.message import EmailMessage
from pygame import mixer #pip install pygame
mixer.init()

#  for pyaudio
#  pip install pipwin
#  pipwin install pyaudio

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

musicdir="D:\\Music"  # add your music folder location
songs = os.listdir(musicdir)

app_id = 'RR8RAK-3P9VK59UJL'

email_list = {'name':'gmail-id'} # add your gmail id in the email_list {'name' : 'gmail_id'}

def fetch_news():
    global news_list
    client = gnewsclient.NewsClient(language='english',location='India', topic='Sports',  max_results=3) 
    news_list = client.get_news()
    
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("\nGOOD MORNING SIR")
    elif(hour>=12 and hour <18):
        speak("GOOD AFTERNOON SIR")
    else:
        speak("GOOD EVENING SIR")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        return "none"
    return query
    
def wikipedia_seach(query):
    speak("searching in wikipedia")
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    speak("according to wikipedia\n")
    speak(results)
    print("\n")

def open_website_or_software(query):
    #query = query.lower()
    if(('command prompt' in query) or ('command' in query)):
        speak('opening command prompt...')    
        os.system("start cmd")
    elif('notepad' in query):
        speak("Opening notepad...")
        os.system("notepad")
    elif(('powerpoint' in query) or ('ppt' in query) or ('power point' in query)):
        speak("Opening Microsoft power point...")
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
    elif (('from youtube' in query) or ('in youtube' in query)):
        if 'open ' in query:
            query=query.replace("open ","")
        youtube(query)
    elif (('word' in query) or ('msword' in query) or ('microsoft word' in query) or ('word document' in query)):
        speak("Opening MICROSOFT WORD...")
        os.system("start winword")
    elif (('excel' in query) or ('msexcel' in query) or ('microsoft excel' in query) or ('excel sheet' in query)):
        speak('Opening microsoft excel sheet . . . ')
        os.system('start excel')
    elif (('google chrome' in query) or('chrome' in query)):
        speak("Opening google chrome . . . ")
        os.system('start chrome')
    else: 
        query=query.replace("open ","")
        while(' ' in query):
            query=query.replace(" ","")
        webbrowser.open('www.'+query+'.com')
        speaking = "opening" + query
        speak(speaking)
    timee.sleep(3)      
    
def search_from_any_website(query):
    if 'search' in query:
        query = query.replace("search ","")
    for j in search(query, tld="co.in", num=3, stop=3, pause=2):
        try:
             webbrowser.open(j)
             break
        except:
            pass
    return speak("openning in website..")

def youtube(query):
    try:
        if "from youtube" in query:
            query = query.replace("from youtube","")
            pywhatkit.playonyt(query)

        elif "in youtube" in query:
            query = query.replace("in youtube","")
            pywhatkit.playonyt(query)
            
        aknoledgment = "playing "+ query
        speak(aknoledgment)
    except:
        google_search(query)
    
def playmusic():
    a= random.randint(0,len(songs))
    speak("playing music...")
    try:
        os.startfile(os.path.join(musicdir,songs[a]))
    except:
        a = random.randint(0,len(songs))
        os.startfile(os.path.join(musicdir,songs[a]))
    timee.sleep(2)
  
def date():
    d = datetime.datetime.today()
    todays_date = "sir,todays date is " + d.strftime("%d %B %Y")
    speak(todays_date)
    
def current_time():
    strTime = datetime.datetime.now().strftime("%I:%M:%S")    
    speak(f"Sir, the time is {strTime}")
    
def news():
    try:		    
        print('Yes sir loading')
        for item in news_list:
            speak("Headlines: "+ item['title'])
            print("\nLink : ", item['link']) 
            print('____________________________________________________________') 
        fetch_news()
    except:
      	speak('An error occured\n')

def wolframalpha_search(query):
    global temp
    temp = query
    try:
        try:
            speak('searching....')
            client = wolframalpha.Client(app_id) 
            if "what is" in query:
                query = query.replace("what is ","")
            elif "which is" in query:
                query = query.replace("which is ","")
            print(query)
            res = client.query(query)
            answer = next(res.results).text
            speak('Got it sir\n')
            speak(answer)
            
        except:
            wikipedia_seach(query)
    except: 
        google_search(temp)
        
def google_search(query):
    global b
    try:
        if 'search in google' in query:
            query=query.replace("search in google","")
        elif 'in google' in query:
            query=query.replace("in google","")
        elif 'from google' in query:
            query=query.replace("from google","")
        webbrowser.open('https://www.google.com/search?q='+query)
        b=1
        speak("opening in google")
    except:
        speak("sorry sir no more result")
        
def working(query):
    
    if 'open' in query:
        global c,b
        open_website_or_software(query)
        c=0
        b=1

    elif ('play music' in query) or ('play any music' in query):
        playmusic()
        timee.sleep(3)
        c=0
        b=1
    
    elif 'time' in query:
        current_time()
        c=0

    elif 'date' in query:
        date()
        c=0
         
    elif ('from youtube' in query) or ('in youtube' in query):
        youtube(query)
        timee.sleep(3)
        c=0
        b=1

    elif 'news' in query:
        news()
        c=0

    elif ('bye' in query) or ('quit' in query) or ('close' in query):
        speak('okay sir, bye..')
        exit()

    elif 'wikipedia' in query:
        c=0
        try: 
            wikipedia_seach(query)
        except:
            ans = search(query, num_results=2)
            webbrowser.open(ans[0])
            b=1

    elif (('search in google' in query) or ('in google' in query) or ('from google' in query)):
        google_search(query)
        c=0
    elif ('search' in query):
        #and ('google' not in query)
        search_from_any_website(query)
        c=0
        b=1

    elif (('what is' in query) or ('which is' in query) or ('weather' in query)) :
        wolframalpha_search(query)
        c=0
    
    elif ('jarvis sleep' in query) or ('sleep mode' in query):
        b=1

    elif ('i want to speak' in query) or ('speak' in query):
        global a
        a=2
        speak("yes sir you can speak whats your query...")

    elif('i want to type' in query) or ('type' in query):
        a=1
        speak("yes sir you can type...")

    elif ('none' not in query):
        speak("Say that again please...\n")

    else:
        c=c+1
        if(c==3):
            b=1    
            
def typing():
    text = input("\nyou--> ")
    return text
  
def speaking():
    query = takeCommand().lower()
    return query
  
def decide_t_or_s(a):
    global query
    if(a==1):
        query = typing()
    elif(a==2):
        query = speaking()
    return query
  
def typeorspeak():
    speak("Do you want to Type or Speak?")
    mode = takeCommand().lower()

    if 'type' in mode:
        global a
        a=1
        speak("yes sir you can type...")
        
    elif 'speak' in mode:
        a=2
        speak("yes sir you can speak whats your query...")
        
    else:
        speak("Invalid CHOICE\n")
        typeorspeak()

if __name__ == "__main__":
    fetch_news()
    wishme()
    t_or_s = typeorspeak()
    global initial
    c=0
    b=0
    initial=0
    query= ' '
    while True:
        if(initial!=0):
            query = decide_t_or_s(a)
        else:
            pass
        if (
            ('wake up jarvis' in query) or (initial==0) or ('wake up' in query) or ('makeup' in query)): #INITIAL = 0 SO NO NEED TO SAY WAKE UP AT BEGINNING
            initial = 1
            if(('wake up jarvis' in query) or ('wake up' in query) or ('makeup' in query)):
                speak("yes sir, I'm wake up")
            while True:
                query = decide_t_or_s(a)
                working(query)
                if(b==1):
                    soundobj = mixer.Sound("Free_Rewind-Swipe-1_REWSE01042.wav")
                    soundobj.play()
                    timee.sleep(1)
                    soundobj.stop()
                    speak("sleep mode\n")
                    b=0
                    c=0
                    break
    
    
#note = i skipped the email and remainder code part , i want you to write better code for sending email without typing and setting remainders without typing
    
    
    
    
    
    
    
    
    
