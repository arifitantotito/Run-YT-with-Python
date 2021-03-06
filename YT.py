import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='id-ID')
            command = command.lower()
            if 'ca' in command:
                command = command.replace('ca', '')
                print(command)
    except:
        pass
    return command

def run_caca():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' +song)
        pywhatkit.playonyt(song)
    else:
        talk('Tidak Terdengar Suaramu Bung!')

run_caca()
