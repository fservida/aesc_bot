# formatters.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 13.06.18


def format_beer_types(beer_types):
    return "\n".join(["*{}* - {}".format(beer_type, description) for beer_type, description in beer_types.items()])