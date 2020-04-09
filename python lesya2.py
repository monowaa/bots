import telebot
from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
  
bot = telebot.TeleBot('1069964716:AAHWBGHkM43eH5CzIFCK9WqpWHjorKE-Ii0')
bot2 = telebot.TeleBot('1182864463:AAGRlHJqLD1BkMOwcSAbev-FC8r4wb9oBs4')
@bot.message_handler(commands=['start'])
def start(message):
    global markup, markup2
    markup = telebot.types.InlineKeyboardMarkup()
    markup2 = telebot.types.InlineKeyboardMarkup()
    button_c = telebot.types.InlineKeyboardButton(text='Отправить свой контакт ☎', callback_data='senddd')
    button1 = telebot.types.InlineKeyboardButton(text='1', callback_data='add1')
    button2 = telebot.types.InlineKeyboardButton(text='2', callback_data='add2')
    button3 = telebot.types.InlineKeyboardButton(text='3', callback_data='add3')
    button4 = telebot.types.InlineKeyboardButton(text='4', callback_data='add4')
    markup.add(button1, button2, button3, button4)
    markup2.add(button_c)
    bot.send_message(chat_id=message.chat.id, text='Some text', reply_markup=markup)
    global chat
    chat = int(message.chat.id)
  
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'add1':
        bot.send_message(chat_id=chat, text='Some text1', reply_markup=markup)
    if call.data == 'add2':
        bot.send_message(chat_id=chat, text='Some text2', reply_markup=markup)
    if call.data == 'add3':
        bot.send_message(chat_id=chat, text='Some text3', reply_markup=markup)
    if call.data == 'add4':
        bot.send_message(chat_id=chat, text='Some text4', reply_markup=markup2)
    if call.data == 'senddd':
        bot.send_message(chat_id=chat, text='number')
        @bot.message_handler()
        def echo_message(msg: types.Message):
            bot.send_message(63850940, text = 'спасибо, с Вами свяжутся')
            bot2.send_message(1001722525, text = msg.from_user.first_name + msg.from_user.last_name)
            bot2.send_message(1001722525, text = msg.text)
            
            
            return start(msg)
            
                
    
        
                
            

    


        
if __name__ == '__main__':
    bot.polling()
