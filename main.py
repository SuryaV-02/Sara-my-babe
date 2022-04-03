from Agent import Agent
from Model import Model

Sara = Agent(1, 170)
text = Sara.listen()
# Sara.speak(text)
print(text)
model = Model()
response = model.process_text(text)
print(response)
Sara.speak(response)

