# commands.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 07.06.18

from aesc_bot.configuration import Configuration
from aesc_bot.utils import build_menu

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import bs4
import feedparser
import os
import errno
import json
import yaml
import requests
from requests import RequestException
from datetime import datetime, timedelta

CACHE_MENU_PATH = "cache/menu/"
ACTIVITIES = os.environ.get("ACTIVITY_YAML",
                            "https://gist.githubusercontent.com/FranceX/d6f03e6c5cc163b801411c327d6e4346/raw/aesc_activities.yml")

cantines = {
    "Amphimax": "amphimax",
    "Centre Sport et Santé": "css",
    "Geopolis": "geopolis",
    "Restaurant de Dorigny": "restaurant-de-dorigny",
    "Unithèque": "unitheque",
}


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


def parse_activities(period):
    try:
        response = requests.get(ACTIVITIES)
        response.raise_for_status()
        activities = yaml.safe_load(response.text)
        if period not in activities:
            raise AssertionError("Wanted period not present")
        activities_formatted = "\n- ".join(
            ["*{}* - {}".format(activity["date"], activity["desc"]) for activity in activities[period]["activities"]])
        message = "{}\n\n- {}".format(activities[period]["desc"], activities_formatted)
    except (RequestException, yaml.YAMLError, AssertionError, KeyError):
        message = "Error parsing activities"

    return message


# summer
def summer(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=parse_activities("summer"), parse_mode='Markdown')


def parse_menu(cantine):
    if not os.path.exists(os.path.dirname(CACHE_MENU_PATH)):
        try:
            os.makedirs(os.path.dirname(CACHE_MENU_PATH))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    cache_path = os.path.join(CACHE_MENU_PATH, "%s.json" % cantine)

    try:
        now = datetime.now()
        cache_last_edit = datetime.fromtimestamp(os.path.getmtime(cache_path))
        if now - cache_last_edit < timedelta(hours=1):
            with open(cache_path) as cache_file:
                assiettes = json.load(cache_file)
        else:
            raise ValueError("Expired cache found, refresh from RSS feed")
    except (FileNotFoundError, ValueError):
        feed = feedparser.parse("https://www2.unil.ch/menus/rss/menu-du-jour/{}".format(cantine))

        assiettes = {}
        if feed.get('entries', False):
            for assiette in feed['entries']:
                assiette_name = assiette['title'].split("-")[1].strip().replace(u'\xa0', ' ')
                assiette_contenu = "\n\t".join([line.strip() for line in
                                                bs4.BeautifulSoup(assiette['summary'],
                                                                  "html.parser").text.strip().strip(
                                                    "\n").split("\n")])
                assiettes[assiette_name] = assiette_contenu
        else:
            assiettes = {"Informations pas disponibles": "Le restaurant est vraisamblablement fermé aujourd'hui"}
        with open(cache_path, "w") as cache_file:
            json.dump(assiettes, cache_file)

    return assiettes


def format_menu(assiettes):
    return "\n".join(
        ["*{}*:\n\t{}".format(assiette_name, assiette_contenu) for assiette_name, assiette_contenu in
         assiettes.items()])


def menu(bot, update):
    button_list = [InlineKeyboardButton(cantine, callback_data="menu_%s" % cantine_rss) for cantine, cantine_rss in
                   cantines.items()]

    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))

    update.message.reply_text("Quelle cantine?", reply_markup=reply_markup)


def menu_handler(bot, update):
    query = update.callback_query
    cantine = query.data.replace("menu_", "")

    assiettes = parse_menu(cantine)

    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=format_menu(assiettes),
                          parse_mode='Markdown')


def version(bot, update):
    conf = Configuration.get_instance()
    bot.send_message(chat_id=update.message.chat_id,
                     text=conf.version)


# echo
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
