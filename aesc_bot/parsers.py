# parsers.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 13.06.18

import requests
from requests import RequestException
import json
import bs4

from pprint import pprint

BEER_TYPES = "https://satellite.bar/bar/biere.php?type_biere=sortes"


def parse_beer_types():
    try:
        response = requests.get(BEER_TYPES)
        html = response.text
    except (RequestException):
        return []

    soup = bs4.BeautifulSoup(html, "html.parser")
    beer_types_raw = soup.select("div#main div.text_block")[2:]

    beer_types = {}
    for beer_type in beer_types_raw:
        try:
            beer = beer_type.select_one("h2").text
            type_desc = " ".join(
                [line.strip() for line in beer_type.select_one("div.text_block_text").text.split("\n")]).strip()

            beer_types[beer] = type_desc

        except AttributeError:
            pass

    return beer_types


def beers_to_json():
    beer_types = parse_beer_types()
    pprint(beer_types)


if __name__ == '__main__':
    beers_to_json()
