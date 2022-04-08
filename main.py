from Agent import Agent
from Model import Model

Sara = Agent(1, 172)
# Sara.soft_speak("Hello there, how can I help you?")
# text = Sara.listen()
text = "Where is Rajalakshmi Engineering College"
print(text)
model = Model()
response = model.process_text(text)
print(response)
Sara.speak(response)