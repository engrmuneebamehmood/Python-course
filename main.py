#text to speech
import pyttsx3
s=input("Enter any text to speak :")

engine= pyttsx3.init()
engine.say(s)
engine.runAndWait()