# bot.py.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 07.06.18

import os
import logging

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from .configuration import Configuration
from .commands import *


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger = Configuration.get_instance().logger
    logger.warning('Update "%s" caused error "%s"', update, error)


def create_bot(**kwargs):
    conf = Configuration.get_instance()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    conf.logger = logger
    conf.help = kwargs.get("command_list", "aesc_bot/command_list.txt")

    updater = Updater(token=os.environ.get("API_KEY", None))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('deadlines', deadlines))
    dispatcher.add_handler(CommandHandler('delai', deadlines))
    dispatcher.add_handler(CommandHandler('summer', summer))
    dispatcher.add_handler(CommandHandler('ete', summer))
    dispatcher.add_handler(CommandHandler('version', version))

    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Log errors
    dispatcher.add_error_handler(error)

    # Start Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
