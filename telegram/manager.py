import os

import telebot
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
bot = telebot.TeleBot(token)


class TelegramManager:
    @staticmethod
    def send_message(message: str) -> None:
        bot.send_message(chat_id, message)



