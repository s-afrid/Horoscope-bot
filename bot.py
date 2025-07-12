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

import requests

def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()

# To launch the bot
bot.infinity_polling()