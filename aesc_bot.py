import os

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import logging

updater = Updater(token=os.environ.get("API_KEY", None))
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ask me anything about the AESC activities!\n\n/help -> Display help")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# help
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="/help -> Display help\n/summer -> Display summer activities\n/ete -> Alias for summer\ndeadlines -> Display importand deadlines\n/delai -> Alias for deadlines")
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def deadlines(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="13 Juin - Rendu 1ere seance travaux de master\n11 Juillet - Rendu 2eme seance travaux de master")
deadlines_handler = CommandHandler('deadlines', deadlines)
delai_handler = CommandHandler('delai', deadlines)
dispatcher.add_handler(deadlines_handler)
dispatcher.add_handler(delai_handler)

# summer
def summer(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Summer! Barbecue Time!\nFête de fin d'année le 22 juin au parc bourget avec bière offerte et grillade!")
summer_handler = CommandHandler('summer', summer)
ete_handler = CommandHandler('ete', summer)
dispatcher.add_handler(summer_handler)
dispatcher.add_handler(ete_handler)

# echo
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

# Start Bot
updater.start_polling()
