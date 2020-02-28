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
keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.row('1', '2', "3")


coins = ['Орел', 'Решка']
gifs = ["https://media.giphy.com/media/1QkVRf2QQ4DCJ7Q115/giphy.gif", "https://media.giphy.com/media/a8TIlyVS7JixO/giphy.gif", "https://media.giphy.com/media/q0ejq5xiOChlS/giphy.gif", 
"https://media.giphy.com/media/38WXjbSM27fIQ/giphy.gif", "https://media.giphy.com/media/o9ZsDfUVEJjy0/giphy.gif"]
doors = [1, 2, 3]
random.shuffle(doors)

def get_opened_door():
    answ1 = list(filter(lambda x: x != car and x != int(choice), doors))[0]
    return answ1

def get_closed_door():
    answ2 = list(filter(lambda x: x != int(choice) and x != get_opened_door(), doors))[0]
    return answ2

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, чем займемся?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'парадокс монти холла':
        bot.send_message(message.chat.id, "Представь, что ты участник игры, в которой тебе нужно выбрать одну из трёх дверей. За одной из дверей находится автомобиль, за двумя другими дверями — козы. Какую дверь выбираешь?", reply_markup=keyboard3)
        bot.register_next_step_handler(message, second_choice)
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

def second_choice(message):
    global choice
    global car
    if message.text.lower() == "1":
        choice = "1"
        car = random.randint(1, 3)
        doorlist = [choice, str(get_closed_door())]
        doorlist.sort()
        keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard4.row(*doorlist)
        goat = open('goat.jpg', 'rb')
        bot.send_message(message.chat.id, f'''Хорошо. Но для начала, я хочу открыть одну из дверей. Мы откроем дверь номер {get_opened_door()} и посмотрим что там.''')
        time.sleep(1)
        bot.send_photo(message.chat.id, goat)
        bot.send_message(message.chat.id, f'''Ой! Тут коза! Ты все еще уверен что хочешь выбрать дверь номер {choice}? ''', reply_markup=keyboard4)
        bot.register_next_step_handler(message, final)
    if message.text.lower() == "2":
        goat = open('goat.jpg', 'rb')
        choice = "2"
        car = random.randint(1, 3)
        doorlist = [choice, str(get_closed_door())]
        doorlist.sort()
        keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard4.row(*doorlist)
        bot.send_message(message.chat.id, f'''Хорошо. Но для начала, я хочу открыть одну из дверей. Мы откроем дверь номер {get_opened_door()} и посмотрим что там.''')
        time.sleep(1)
        bot.send_photo(message.chat.id, goat)
        bot.send_message(message.chat.id, f'''Ой! Тут коза! Ты все еще уверен что хочешь выбрать дверь номер {choice}? ''', reply_markup=keyboard4)
        bot.register_next_step_handler(message, final)
    if message.text.lower() == "3":
        goat = open('goat.jpg', 'rb')
        choice = "3"
        car = random.randint(1, 3)
        doorlist = [choice, str(get_closed_door())]
        doorlist.sort()
        keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard4.row(*doorlist)
        bot.send_message(message.chat.id, f'''Хорошо. Но для начала, я хочу открыть одну из дверей. Мы откроем дверь номер {get_opened_door()} и посмотрим что там.''')
        time.sleep(1)
        bot.send_photo(message.chat.id, goat)
        bot.send_message(message.chat.id, f'''Ой! Тут коза! Ты все еще уверен что хочешь выбрать дверь номер {choice}? ''', reply_markup=keyboard4)
        bot.register_next_step_handler(message, final)

def final (message):
    if int(message.text.lower()) == car:
        car_photo = open('car.png', 'rb')
        bot.send_photo(message.chat.id, car_photo)
        link_markup = telebot.types.InlineKeyboardMarkup()
        link_hall= telebot.types.InlineKeyboardButton(text='Почитать про парадокс', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%B4%D0%BE%D0%BA%D1%81_%D0%9C%D0%BE%D0%BD%D1%82%D0%B8_%D0%A5%D0%BE%D0%BB%D0%BB%D0%B0')
        link_markup.add(link_hall)
        bot.send_message(message.chat.id, "Поздравляем! Ты выиграл ааааавтомобиль!", reply_markup=link_markup)
        time.sleep(1)
        bot.send_message(message.chat.id, "Чем теперь займемся?", reply_markup=keyboard1)
    elif int(message.text.lower()) != car:
        goat2 = open('goat_2.jpg', 'rb')
        bot.send_photo(message.chat.id, goat2)
        link_markup = telebot.types.InlineKeyboardMarkup()
        link_hall= telebot.types.InlineKeyboardButton(text='Почитать про парадокс', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%B4%D0%BE%D0%BA%D1%81_%D0%9C%D0%BE%D0%BD%D1%82%D0%B8_%D0%A5%D0%BE%D0%BB%D0%BB%D0%B0')
        link_markup.add(link_hall)
        bot.send_message(message.chat.id, "Эх, тебе досталась коза", reply_markup=link_markup)
        time.sleep(1)
        bot.send_message(message.chat.id, "Чем теперь займемся?", reply_markup=keyboard1)

    

# @bot.message_handler(content_types=['document'])
# def sticker_id(message):
#         print (message)

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
