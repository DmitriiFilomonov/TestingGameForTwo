class Code(object):
	def __init__(self, text_code = [], bugs = {}):
		self.text_code = text_code
		self.bugs = bugs


class Player(object):

	def __init__(self, name = "Player"):
		self.name = name
		self.score = 0
		self.activ = True


class Game(object):

	def __init__(self):
		self.code = Code()
		self.player1 = Player()
		self.player2 = Player()


def main():
	print("Hello world")


if __name__ == '__main__':
	main()
