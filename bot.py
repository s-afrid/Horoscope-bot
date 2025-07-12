# Exported environment variable and created a bot out of it using Telebot()
import os
import telebot
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
# Message handler like /start or /hello to send welcome message
@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    bot.reply_to(message, 'Hello and Welcome, I am your Horoscope bot!')

# Echo back the message handler
@bot.message_handler(func = lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message)

# To launch the bot
bot.infinity_polling()