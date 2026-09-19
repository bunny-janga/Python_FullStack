'''
gTTS --> google text to speech

from gtts import gTTS
text = gTTS("hello guys, how are you doing")
text.save("audio.mp3")
'''
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os

#let us create listen function
def listen():
    """Function for Speech Recognition"""
    r=sr.Recognizer()
    #we will take microphone as source
    with sr.Microphone() as source:
        print('ika modhaledadhamaa')
        audio=r.listen(source,phrase_time_limit=5)#10 seconds
    #we need to give our text as voice
    data=""
    #here we will give exceptions(try, except)
    try:
        data=r.recognize_google(audio,language='en-US')
        print('You said:',data)
    except sr.UnknownValueError as e:
        print('Request Failed')
    except sr.RequestError as e:
        print('Speak clearly request is failing')
    return data
    #tts=gTTS(data)
    #tts.save('new.mp3')
    #playsound.playsound('new.mp3')
#listen() 

def respond(String):
    """Function to respond back"""
    print(String)
    tts=gTTS(String)
    tts.save('Speech.mp3')
    #we are using uuid --> to randomize the content in the audio file
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
  

#here we will make our virtual assitant into action
def va(data):
    """Our Virtual Assistant with the actions"""
    if "how are you" in data:
        listening=True
        respond('I am fine, thanks for asking')
    elif 'what are your plans' in data:
        listening=True
        respond('Only study... one focus in 2026')
    elif 'how are things going' in data:
        listening=True
        respond('Antha okay ika nene set avvali')
    elif 'time' in data:
        listening=True
        respond(time.ctime())
    elif 'stop talking' in data:
        listening=False
        respond('Okay cool... kopadakuu bye')
    elif "locate" in data:
        listening = True
        webbrowser.open("https://www.google.com/maps/search/"+ data.replace("locate",""))
    try:
        return listening
    except UnboundLocalError as e:
        print('Make sure to speak louder and faster')

respond('Hey noam ... Good to hear from you. How are you?')
listening=True
while listening:
    data=listen()
    listening=va(data)

