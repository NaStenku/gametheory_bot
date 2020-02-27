import telebot
import random
import time
from flask import Flask, request
import os

TOKEN = '731187754:AAE4Z-g-KEMtBBL8vZq-rykJVobm3EsTB8A'
bot = telebot.TeleBot(token = TOKEN)
server = Flask(__name__)

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Подбрось монетку', 'Парадокс Монти Холла')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Бросай', 'Я передумал')

coins = ['Орел', 'Решка']
gifs = ["https://media.giphy.com/media/1QkVRf2QQ4DCJ7Q115/giphy.gif", "https://media.giphy.com/media/a8TIlyVS7JixO/giphy.gif", "https://media.giphy.com/media/q0ejq5xiOChlS/giphy.gif", 
"https://media.giphy.com/media/38WXjbSM27fIQ/giphy.gif", "https://media.giphy.com/media/o9ZsDfUVEJjy0/giphy.gif"]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, чем займемся?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'парадокс монти холла':
        bot.send_message(message.chat.id, 'Я еще над этим работаю.', reply_markup=keyboard1)
    elif message.text.lower() == 'подбрось монетку':
        bot.send_message(message.chat.id, 'Итак, я держу монетку. Бросаем?', reply_markup=keyboard2)
        bot.register_next_step_handler(message, flip)
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

def flip(message): 
    if message.text.lower() == 'бросай':
        bot.send_message(message.chat.id, 'Но ты ведь знаешь, что решение принимается тогда, когда монетка еще в полете? Она летиииит')
        bot.send_document(message.chat.id, random.choice(gifs))
        time.sleep(3)
        bot.send_message(message.chat.id, random.choice(coins), reply_markup=keyboard1)
    elif message.text.lower() == 'я передумал':
        bot.send_message(message.chat.id, 'Ну как хочешь. Так чем займемся?', reply_markup=keyboard1)

    

@bot.message_handler(content_types=['document'])
def sticker_id(message):
        print (message)

@server.route ('/' + TOKEN, methods = ["POST"])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route ('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url = "https://stormy-dusk-68640.herokuapp.com/" + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host ="0.0.0.0", port = int(os.environ.get("PORT", 5000)))
