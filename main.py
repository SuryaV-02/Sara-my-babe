from Agent import Agent
from Model import Model

import traceback
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBPxb07ns_mGf76YTQ0yXkGV6ytlXKolsc",
    "authDomain": "sara-memory.firebaseapp.com",
    "databaseURL": "https://sara-memory-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "sara-memory",
    "storageBucket": "sara-memory.appspot.com",
    "messagingSenderId": "356595803238",
    "appId": "1:356595803238:web:d4e77f5d01acc8b939b9a7",
    "measurementId": "G-8B0Q4DZTKS"
}
firebase = pyrebase.initialize_app(firebaseConfig)


def signing_up():
    auth = firebase.auth()
    email = input('Enter Email : ')
    password = input('Enter Password : ')
    try:
        auth.create_user_with_email_and_password(email, password)
        print('Created user ', email)
        return 1
    except Exception:
        traceback.print_exc()
        return 0


def signing_in():
    auth = firebase.auth()
    email = input('Email : ')
    password = input('Password : ')
    try:
        auth.sign_in_with_email_and_password(email, password)
        print('Signed in as ', email)
        return 1
    except Exception:
        traceback.print_exc()
        return 0


def recognize_person():
    print('Please sign up to get started!')
    Sara.speak('Please sign up to get started!')
    name = input('Name : ')
    if signing_up() == 1:
        print(('Now, signin..'))
        Sara.speak('Now, signin..')

        if (signing_in() == 1):
            Sara.speak('Welcome Surya')
            print('Welcome', name)
    else:
        print('Sorry, I cannot recognize you ..')
        Sara.speak('Sorry, I cannot recognize you ..')


Sara = Agent(1, 172)
model = Model()

print("Hello there, how can I help you?")
Sara.speak("Hello there, how can I help you?")
while True:
    text = Sara.listen()
    # text = input("Enter your request : ")
    print(text)
    if text is not None:
        response = model.process_text(text)
        print(response)
        Sara.speak(response)
