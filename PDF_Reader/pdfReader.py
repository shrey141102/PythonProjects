import os
import pyttsx3
import speech_recognition as sr
import PyPDF2

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

def readBooks():
    speak("Enter the path of the file including it's name.")
    filePath = input("Enter the path of the file (including it's name): ")
    try:
        os.startfile(filePath)
        book = open(filePath, 'rb')
        pdfreader = PyPDF2.PdfReader(book)
        pages = len(pdfreader.pages)
        speak(f"Number of pages in this books are {pages}")

        speak("From Which Page I Have To Start Reading ?")
        speak("Please write the page number: ")
        numPage = int(input("Enter the Page number: "))

        page = pdfreader.pages[numPage-1]
        text = page.extract_text()
        speak(text)
    except:
        speak("Sorry, This Book is not Present!")

readBooks()
