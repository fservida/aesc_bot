# commands.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 07.06.18

from .configuration import Configuration

# start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Ask me anything about the AESC activities!\n\n/help -> Display help")


# help
def help(bot, update):
    conf = Configuration.get_instance()
    bot.send_message(chat_id=update.message.chat_id,
                     text=conf.help)


def deadlines(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="13 Juin - Rendu 1ere seance travaux de master\n11 Juillet - Rendu 2eme seance travaux de master")


# summer
def summer(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Summer! Barbecue Time!\nFête de fin d'année le 22 juin au parc bourget avec bière offerte et grillade!")


def version(bot, update):
    conf = Configuration.get_instance()
    bot.send_message(chat_id=update.message.chat_id,
                     text=conf.version)

# echo
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)