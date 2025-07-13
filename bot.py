# Exported environment variable and created a bot out of it using Telebot()
import os
import telebot
from utilis import get_daily_horoscope
BOT_TOKEN = '7982603841:AAEy1-iJwBlqRxDokiCJ17chl_5OMPsVfeI'
#BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
# Message handler like /start or /hello to send welcome message
@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    bot.reply_to(message, 'Hello and Welcome, I am your Horoscope bot!')

@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message):
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())
    
def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")

# Echo back the message handler
@bot.message_handler(func = lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message)


# To launch the bot
bot.infinity_polling()