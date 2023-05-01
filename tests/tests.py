import unittest
import sys

sys.path.append('../')
from main import *


class TestGame(unittest.TestCase):
	def test_class_Code(self):
		code = Code(text_code, bags)
		self.assertIsNotNone(code)

	def test_class_Player(self):
		player = Player("Tim")
		self.assertIsNotNone(player)

	def test_class_Game(self):
		game = Game()
		self.assertIsNotNone(game)


if __name__ == '__main__':
	unittest.main()
