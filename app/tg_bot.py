import telebot
from telebot import types

from db.engine import create_db
from db.crud import insert_message
from config import settings

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    insert_message({'name': message.text})
    bot.send_message(message.chat.id, f'{message.text} - message was inserted to DB.')


if __name__ == "__main__":
    create_db()
    bot.infinity_polling()
