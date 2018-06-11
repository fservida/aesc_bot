# commands.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 10.06.18

import unittest
import random
from aesc_bot.commands import parse_menu, cantines


class TestWebRequests(unittest.TestCase):

    def test_menu(self):
        # Fetch from Unil
        for cantine in cantines.values():
            self.assertNotEqual(parse_menu(cantine), "")
        # Fetch a random sample from cached file (Second run)
        self.assertNotEqual(parse_menu(list(cantines.values())[random.randint(0, len(cantines) - 1)]), "")


if __name__ == '__main__':
    unittest.main()
