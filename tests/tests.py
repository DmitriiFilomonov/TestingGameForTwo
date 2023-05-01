import unittest
import sys

sys.path.append('../')
from main import *


class TestGame(unittest.TestCase):
	def test_class_Code(self):
		code = Code()
		self.assertIsNotNone(code)
		code.text_code = ["abcd = 666", "prints(abcd)"]
		code.bugs = {1: "abcd = int(666)", 2: "print(abcd)"}
		self.assertEqual(code.text_code, ["abcd = 666", "prints(abcd)"])
		self.assertEqual(code.bugs, {1: "abcd = int(666)", 2: "print(abcd)"})

	def test_class_Player(self):
		player = Player()
		self.assertIsNotNone(player)
		player.name = "Tim"
		player.score = 3
		player.activ = True
		self.assertEqual(player.name, "Tim")
		self.assertEqual(player.score, 3)
		self.assertTrue(player.activ)

	def test_class_Game(self):
		game = Game()
		self.assertIsNotNone(game)
		self.assertIsInstance(game.code, Code)
		self.assertIsInstance(game.player1, Player)
		self.assertIsInstance(game.player2, Player)

	def test_get_activ_player(self):
		game = Game()
		self.assertFalse(game.get_activ_player().activ)

	def test_check_num_in_bugs(self):
		game = Game()
		self.assertLessEqual(2, len(game.code.text_code))

	def test_repeating_responses(self):
		answers = {1: "abcd = int(666)"}
		answer = "abcd = int(666)"
		self.assertEqual(answer, answers[1])

if __name__ == '__main__':
	unittest.main()
