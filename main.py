class Code(object):
	def __init__(self, text_code = [], bugs = {}):
		self.text_code = text_code
		self.bugs = bugs


class Player(object):

	def __init__(self, name = "Player"):
		self.name = name
		self.score = 0
		self.activ = True

	def set_activ_status(self, bool_value):
		self.activ = bool_value


class Game(object):

	def __init__(self):
		self.code = Code()
		self.player1 = Player()
		self.player2 = Player()

	def get_activ_player(self):
		if self.player1.activ:
			print("Начинает игрок №1", self.player1.name)
			self.player1.set_activ_status(False)
			self.player2.set_activ_status(True)
			return self.player1
		else:
			print("Начинает игрок №2", self.player2.name)
			self.player1.set_activ_status(True)
			self.player2.set_activ_status(False)
			return self.player2

	def start_game(self):
		total_account = 0
		answers = dict()
		total_errors = len(self.code.bugs)

		while total_account < total_errors:
			activ_player = self.get_activ_player()
			break


def main():
	Game().start_game()


if __name__ == '__main__':
	main()
