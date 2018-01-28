# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import hashlib
import serial
ser = serial.Serial('COM5', 9600, timeout=2)

bot = telebot.TeleBot(config.token)

def check_user(chat_id):
    with open ('chat.txt','r', encoding='utf-8') as p:
        chats = p.read().split()
        print(chats, chat_id)
    if str(chat_id) in chats:
        return True
    return False
def add_user(chat_id):
    with open ('chat.txt','a',encoding='utf-8') as p:
        p.write(chat_id)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Для доступа введите пароль')

@bot.message_handler(regexp="i_love_Mary")
def handle_password (message):
    add_user(str(message.chat.id))
    bot.send_message(message.chat.id, 'Доступ открыт')



@bot.message_handler(commands=['water_the_plants'])
def handle_cat(message):
    if check_user(message.chat.id):
        ser.write(b'1')
        bot.send_message(message.chat.id, 'Цветы политы')
        ser.write(b'0')
    else:
        bot.reply_to(message, 'Введи пароль в формате "passwоrd пароль"')
    

bot.polling()
