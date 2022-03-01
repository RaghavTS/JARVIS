import datetime
import os
import subprocess
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.say("What kind of voice would you like for your virtual assistant ")
engine.runAndWait()
sound = input("F or M?  ")
if sound == 'M':
    engine.say('select a name for your virtual assistant')
    engine.runAndWait()
    name_va = input("Name your virtual assistant:  ")
    engine.setProperty('voice', voices[0].id)
    engine.say('Hi. I am ' + name_va + '. How can I help you')
    engine.runAndWait()
elif sound == 'F':
    engine.setProperty('voice', voices[1].id)
    engine.say('select a name for your virtual assistant')
    engine.runAndWait()
    name_va = input("Name your virtual assistant:  ")
    engine.say('Hi. I am ' + name_va + '. How can I help you')
    engine.runAndWait()
else:
    print('invalid entry')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name_va in command:
                command = command.replace(name_va, '')
                print(command)
    except:
        pass
    return command


runvar = True
while runvar == True:
    time.sleep(5)
    command = take_command
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H %M')
        talk('the time is' + time)
        print('the time is ' + time)
    elif 'joke' in command:
        joke = pyjokes.get_joke('en')
        talk(joke)
        print(joke)
    elif 'name' in command:
        talk("My name is Monty")
    elif 'dna' in command:
        talk("Enter the DNA sequence:")
        sequence = input("Sequence(USE A,t,G,c as input):  ")
        dna1 = sequence.replace('A', 'T')
        dna2 = dna1.replace('t', 'a')
        dna3 = dna2.replace('G', 'C')
        dna4 = dna3.replace('c', 'g')
        print('The second strand is: ' + dna4)
        rna = dna4.replace('T', 'U')
        print('The mRNA sequence is:         ' + rna)
        rna2 = sequence.replace('t', 'U')
        print('The second strand of mRNA is: ' + rna2)
        talk('Here are the DNA and mRNA sequences')
    elif 'who is' in command:
        person = command.replace('who is', '')
        about_person = wikipedia.summary(person, 1)
        print(about_person)
        talk(about_person)
    elif 'open matlab' in command:
        talk('opening matlab. Good luck with your coding.')
        subprocess.call('C://Program Files//MATLAB//R2021a//bin//matlab.exe')
    elif 'open teams' in command:
        talk('opening teams. Happy meeting.')
        subprocess.call('C://Users//tsrag//AppData//Local//Microsoft//Teams//Update.exe --processStart "Teams.exe"')
    elif 'open chrome' in command:
        talk('opening chrome. Keep your history clean')
        subprocess.call("C://Program Files//Google//Chrome//Application//chrome.exe")
    elif 'message' in command:
        talk('Type the phone number of the reciever')
        phn = input("Ph:")
        with sr.Microphone() as source_of_msg:
            talk('What is the message')
            message = listener.listen(source_of_msg)
            msg = listener.recognize_google(message)
            talk('sending message')
        pywhatkit.sendwhatmsg_instantly('+91' + phn, msg, 5)
    elif 'send a mail' in command:
        with sr.Microphone() as source_of_mail:
            talk('What is the subject')
            subject_voice = listener.listen(source_of_mail)
            sbj = listener.recognize_google(subject_voice)
        with sr.Microphone() as source_of_body:
            talk('Dictate the body of the letter')
            body_voice = listener.listen(source_of_body)
            body = listener.recognize_google(body_voice)
        talk('Type the email ID of the reciever')
        email = input("Email id: ")
        pywhatkit.send_mail('tsraghav11@gmail.com', 'C5H4NC4H7NCH3', sbj, body, email)
    elif 'google' in command:
        argument = command.replace('google', '')
        talk('searching for ' + argument)
        pywhatkit.search(argument)
    elif 'edit my browser' in command:
        pywhatkit.search("chrome://flags")
    elif 'open my project files' in command:
        talk('opening your project files')
        os.startfile("C://Users//tsrag//OneDrive//Desktop//project")
    elif 'thanks' in command:
        talk('You are welcome')
    elif 'what is' in command:
        thing = command.replace('what is', '')
        about_thing = wikipedia.summary(thing)
        print(about_thing)
        talk('Here is the information about' + thing + 'according to wikipedia')
    elif 'bye' in command:
        runvar = False
    else:
        talk(' Sorry. I did not understand' + command + 'Please repeat')
