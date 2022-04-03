import pyttsx3
import speech_recognition as sr
import pyaudio


class Agent(object):
    def __init__(self, gender: int, speech_rate: int) -> object:
        self.agent = pyttsx3.init()
        voices = self.agent.getProperty('voices')
        self.voice = voices[gender].id
        self.speech_rate = speech_rate
        self.agent.setProperty('voice', self.voice)
        self.agent.setProperty('rate', self.speech_rate)
        self.r = sr.Recognizer()
        print('Created agent')

    def speak(self, text):
        self.agent.say(text)
        self.agent.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as mic:
                self.r.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.r.listen(mic)
                text = self.r.recognize_google(audio)
                text = text.lower()
                return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")
