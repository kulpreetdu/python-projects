from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as py
import speech_recognition as sp
import threading

engine=py.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

conversation =['hello','Hi There!',
                'hi','Hi There!',
                'who created you','I am Cooking ML Chatbot',
               'what is your name','My name is Cooking Bot',
               'in which languages you speak','I speak in English',
               'in which city you live','I live in Ghaziabad',
               'how are you?','I am Great',
               'how to cook maggi','Firstly, boil water in the pan and add some salt in it and then break the maggi and add in the hot water and then lastly add maggi magic masala in it and serve it',
               'how to cook pasta','Firstly, boil water in the pan and add some salt in it and then add pasta in the hot water and boil it and then take it out after 10 min when it is cooked and then lastly add  masala in it and serve it',
               'how to boil potatoes','Firstly, boil water in the cooker and add some salt in it and then wash the potatoes in water and add in the cooker and then lastly wait for 10 to 15 minutes for the wishtle to come and serve it',
               ]

trainer = ListTrainer(bot)
trainer.train(conversation)


main = Tk()
main.geometry("600x600")
main. title("My Cooking Bot")

def take_query():
    sr=sp.Recognizer()
    sr.pause_threshold=1
    with sp.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            textf.delete(0,END)
            textf.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognised")

def ask_from_bot():
    query=textf.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you: "+query)
    msgs.insert(END,"bot: "+str(answer_from_bot))
    speak(answer_from_bot)
    textf.delete(0,END)
    msgs.yview(END)


frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame, width=600,height=20,yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=RIGHT, fill=BOTH)
frame.pack()

textf = Entry(main, font=("Verdana", 20))
textf.pack(fill=X,pady=10)

btn=Button(main, text="Ask from Bot",font=("Verdana", 20),command=ask_from_bot)
btn.pack()

def repeat():
    while True:
        take_query()

t=threading.Thread(target=repeat)
t.start()

main.mainloop()