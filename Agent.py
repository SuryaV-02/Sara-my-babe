import pyttsx3
import speech_recognition as sr
import pyaudio
# For soft speak
import wolframalpha

from gtts import gTTS
from playsound import playsound
import os

class Agent(object):
    def __init__(self, gender: int, speech_rate: int) -> object:
        self.agent = pyttsx3.init()
        voices = self.agent.getProperty('voices')
        self.voice = voices[gender].id
        self.speech_rate = speech_rate
        self.agent.setProperty('voice', self.voice)
        self.agent.setProperty('rate', self.speech_rate)
        self.r = sr.Recognizer()
        # print('Created agent')

    def soft_speak(self,text):
        tts = gTTS(text=text, lang="en",slow=False)
        filename = os.path.dirname(__file__) + "\\voice.mp3"
        tts.save(filename)
        playsound(filename)

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
        except TypeError as e:
            # print("Could not request results; {0}".format(e))
            # print('Nothing heard')
            pass
        except Exception as ex:
            # print('Nothing heard 2')
            return None
        except sr.UnknownValueError:
            print("unknown error occurred")
            return None
