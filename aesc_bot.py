from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import logging

updater = Updater(token='567528274:AAFefGLjHw6Fcu7GPE4wWkR_eXGPixVbYtQ')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ask me anything about the AESC activities!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# summer
# start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Summer! Barbecue Time!\nFête de fin d'année le 22 juin au parc bourget avec bière offerte et grillade!")
start_handler = CommandHandler('summer', start)
dispatcher.add_handler(start_handler)

# echo
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

# Start Bot
updater.start_polling()
