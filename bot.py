#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from config import API_TOKEN
from main import generate_image
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Photobot.
Я создаю картинки по промту!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def photo_message(message):
    bot.reply_to(message, message.text)
    prompt = message.text

    filename = generate_image(prompt, "image.jpg")

    with open(filename, "rb") as photo:
        bot.send_photo(message.chat.id, photo)





bot.infinity_polling()