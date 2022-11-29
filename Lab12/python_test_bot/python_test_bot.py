from telegram import *
from telegram.ext import *
from requests import *

with open('python_test_bot/token.txt', 'r', encoding='utf-8') as token_file:
    token = token_file.read()


def start(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('Почати тест'), KeyboardButton('Допомога')]]
    welcome_text = """
    Лабораторна робота №12. 
    Виконав студент групи ВТ-21-1(1) Бабушко Андрій. 
    
    Виберіть один із запропонованих пунктів меню нижче:
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text, reply_markup=ReplyKeyboardMarkup(buttons))


updater = Updater(token)

updater.dispatcher.add_handler('start', start)

updater.start_polling()
updater.idle()
