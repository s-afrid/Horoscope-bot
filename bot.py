import os
import telebot
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
# Exported environment variable and created a bot out of it using Telebot()
