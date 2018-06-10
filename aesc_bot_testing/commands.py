# commands.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 10.06.18

from aesc_bot.commands import parse_menu


def test_menu(cantine = "amphimax"):
    formatted_menu = parse_menu(cantine)
    if formatted_menu == "":
        raise ValueError("The formatted menu is an empty string")