import telebot
from telebot import types
import json


token='5178608519:AAGqDLaQzbTEuyaGC5R9-LoZ45Y_8DxQ3Qg'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types='text')
def start_message(message):
    # if message.text == 'ok':
    try:
        bot.send_message(message.chat.id, message.text)
    except Exception as _ex:
        bot.send_message(message.chat.id, _ex)
    # bot.send_message(message.chat.id, 'Привет')
    # markup = types.ReplyKeyboardMarkup(row_width=2)
    # itembtn1 = types.KeyboardButton('Чек')
    # itembtn2 = types.KeyboardButton('Счет на оплату')
    # itembtn3 = types.KeyboardButton('Договор')
    # markup.add(itembtn1, itembtn2, itembtn3)
    # bot.send_message(message.chat.id, "Выберите вид документа:", reply_markup=markup)


# @bot.message_handler(content_types='text')
# def text_message(message):
#     if message.text == "Договор":
#         pass
#         # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         # item1 = types.KeyboardButton
#         # markup.
#         # bot.send_message(message.chat.id, 'пока не работет', reply_markup=markup)
#     elif message.text == "Чек":
#         bot.send_message(message.chat.id, 'пока не работает')
#     elif message.text == "Счет на оплату":
#         bot.send_message(message.chat.id, 'Сделайте фото')
#     else:
#         bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['document', 'audio','photo'])
def photo_reply(message):
    bot.send_message(message.chat.id, "Сохранил!")
    pass



@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

bot.infinity_polling()