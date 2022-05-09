# data driven assistant
import pyttsx3 
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyaudio

def assistant(audio):

    engine = pyttsx3.init()

    # get current engine voice options

    voices = engine.getProperty('voices')
    
    # set [0] for male voice, [1] for female voice

    engine.setProperty('voices', voices[1].id)

    # speak audio message with said voice

    engine.say(audio)

    # wait for processes to finish

    engine.runAndWait()

def greeting():

    # a simple greeting that informs user that assistant has started

    assistant("Hello, I am your Virtual Assistant, CARLA. How can I help you today?")


def audioinput():
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening and processing')
        aud.pause_threshold = 0.7
        audio.aud.listen(source)

    try:
        print("understanding")

        phrase = aud.recognize_google(audio, language='en-us')
        print("you said: ", phrase)
    except Exception as exp:
        print(exp)
        print("Can you please repeat that")
        return "None"

    return phrase

def theTime(self):
    time = str(datetime.datetime.now())

    print(time)

    hour = time[11:13]
    minute = time[14:16]

    assistant(self, "The time right now is" + "Hours and" + minutes + "Minutes")

def theDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
            }

    if day in Day_dict.keys():
        weekday = Day_dict[day]
        print(weekday)
        assistant("it's " + weekday)

def core_code():
    greeting()

    while (True):
        phrase = audioinput().lower()

    if "open medium" in phrase:
        assistant("Opening Medium.com")
        webbrowser.open("www.medium.com")
    elif "open google" in phrase:
        assistant("Opening Google")
        webbrowser.open("www.google.com")
    elif "what day is it" in phrase:
        theDay()
    elif "what time is it" in phrase:
        theTime()
    elif "bye" in phrase:
        assistant("Exiting. Have a Good Day")
        exit()
    elif "from wikipedia" in phrase:
        assistant("Checking the wikipedia")
        phrase = phrase.replace("wikipedia", "")
        result = wikipedia.summary(phrase, sentences=4)
        assistant("As per wikipedia")
        assistant(result)
    elif "what is your name" in phrase:
        assistant("I am Carla")

core_code()




