import telebot
import random
import time
bot = telebot.TeleBot('731187754:AAE4Z-g-KEMtBBL8vZq-rykJVobm3EsTB8A')

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Подбрось монетку', 'Парадокс Монти Холла')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Бросай', 'Я передумал')

coins = ['Орел', 'Решка']



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
        bot.send_animation(message.chat.id, 'https://i.gifer.com/Ilp.gif')
        time.sleep(3)
        bot.send_message(message.chat.id, random.choice(coins), reply_markup=keyboard1)
    elif message.text.lower() == 'я передумал':
        bot.send_message(message.chat.id, 'Ну как хочешь. Так чем займемся?', reply_markup=keyboard1)

    

@bot.message_handler(content_types=['document'])
def sticker_id(message):
        print (message)

  


bot.polling(none_stop=True)