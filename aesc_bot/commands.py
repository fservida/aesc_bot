# commands.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 07.06.18

from aesc_bot.configuration import Configuration
# import requests
import bs4
# import html

from pprint import pprint

import feedparser

cantine_names = {
    "unitheque": ("uni", "unitheque", "banane", "unithèque"),
    "amphimax": ("amphi", "amphimax", "max"),
    "geopolis": ("geopolis", "géopolis"),
    "css": ("css", "sport", "centre sport et santé"),
    "restaurant-de-dorigny": ("da nino", "restaurant de dorigny")
}

cantine_names_reverse = {}
for cantine, aliases in cantine_names.items():
    for alias in aliases:
        cantine_names_reverse[alias] = cantine


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


def parse_menu(cantine):

    feed = feedparser.parse("https://www2.unil.ch/menus/rss/menu-du-jour/{}".format(cantine))

    assiettes = {}
    for assiette in feed['entries']:
        assiette_name = assiette['title'].split("-")[1].strip().replace(u'\xa0', ' ')
        assiette_contenu = "\n\t".join([line.strip() for line in bs4.BeautifulSoup(assiette['summary'], "html.parser").text.strip().strip("\n").split("\n")])
        assiettes[assiette_name] = assiette_contenu

    return assiettes


def format_menu(assiettes):
    return "\n".join(
        ["*{}*:\n\t{}".format(assiette_name, assiette_contenu) for assiette_name, assiette_contenu in assiettes.items()])


def menu(bot, update, args):
    cantine = " ".join(args)
    cantine = cantine_names_reverse.get(cantine, None)

    if cantine is not None:
        assiettes = parse_menu(cantine)

        bot.send_message(chat_id=update.message.chat_id,
                         text=format_menu(assiettes), parse_mode='Markdown')
    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Pas de cantine specifié, eg. utilisation: */menu* banane\n", parse_mode='Markdown')


def version(bot, update):
    conf = Configuration.get_instance()
    bot.send_message(chat_id=update.message.chat_id,
                     text=conf.version)


# echo
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


if __name__ == '__main__':
    assiettes = parse_menu("unitheque")
    print(format_menu(assiettes))
