# commands.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 10.06.18

from aesc_bot.commands import parse_menu, format_menu


def test_menu(cantine = "amphimax"):
    assiettes = parse_menu(cantine)
    formatted_menu = format_menu(assiettes)
    if formatted_menu == "":
        raise ValueError("The formatted menu is an empty string")


if __name__ == '__main__':
    test_menu()