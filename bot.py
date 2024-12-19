import os
from dotenv import load_dotenv
from telebot import TeleBot

# Загрузка переменных окружения
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    welcome_text = (
        "Добро пожаловать в Whieda Assistant! \n"
        "Выберите категорию продукции или задайте вопрос."
    )
    bot.reply_to(message, welcome_text)

bot.polling()

