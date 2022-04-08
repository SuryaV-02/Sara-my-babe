from gtts import gTTS
from playsound import playsound
import os

def speak(txt):
    tts=gTTS(text=txt,lang="en")
    filename = os.path.dirname(__file__) + "\\voice.mp3"
    tts.save(filename)
    # os.path.dirname(__file__) + "\\voice.mp3"
    playsound(filename)

speak('Hello da')