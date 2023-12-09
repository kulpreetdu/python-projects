from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

DB = {
    'drivername': 'mysql',
    'host': '127.0.0.1',
    'port': '3306',
    'username': os.environ.get('DBUNAME'),
    'password': os.environ.get('DBPASS'),
    'database': os.environ.get('DBNAME'),
    'query': {'charset':'utf8'}
}

engine = create_engine(URL(**DB))

bot = ChatBot("My Bot")

conversation =['hello','Hi There!',
               'what is your name','My name is Cooking Bot',
               'in which languages you speak','I speak in English',
               'in which city you live','I live in Ghaziabad',
               'how are you?','I am Great',
               'how to cook maggi','Firstly, boil water in the pan and add some salt in it and then break the maggi and add in the hot water and then lastly add maggi magic masala in it and serve it',
               'how to cook pasta','Firstly, boil water in the pan and add some salt in it and then add pasta in the hot water and boil it and then take it out after 10 min when it is cooked and then lastly add  masala in it and serve it',
               ]

trainer = ListTrainer(bot)

trainer.train(conversation)

answer = bot.get_response('hello')
print(answer)