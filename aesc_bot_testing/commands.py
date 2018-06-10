# commands.py
# Project: aesc_bot
# 
# Created by "Francesco Servida"
# Created on 10.06.18

import unittest
from aesc_bot.commands import parse_menu


class TestWebRequests(unittest.TestCase):

    def test_menu(self):
        self.assertNotEqual(parse_menu("amphimax"), "")


if __name__ == '__main__':
    unittest.main()