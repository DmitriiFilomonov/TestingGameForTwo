class Code(object):
	def __init__(self, text_code = ["abcd = 666", "prints(abcd)"], bugs = {1: "abcd = int(666)", 2: "print(abcd)"}):
		self.text_code = text_code
		self.bugs = bugs

	def get_test_code_text(self):
		i = 1
		text_code_file = open("text_code1.txt", "r")
		print()
		for line in text_code_file:
			print(i, line)
			self.text_code.append(line)
			i += 1
		text_code_file.close()
		print()


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
		self.bags_list = {1: {2:"    if n <= 1:", 
					 6:"        for i in range(1, n):", 
					 7: "            m, k = k, (m+k)%10", 
					 13: "    print(fib_digit(n))", 
					 16:'''if __name__ == "__main__":''',
					 17: "    main()"}}

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

	def check_num_in_bugs(self):
		num = len(self.code.text_code)+1
		while num > len(self.code.text_code):
			num = int(input("Введите номер строки, в которой вы видите ошибку - "))
		return num

	def check_winner(self):
		if self.player1.score == self.player2.score:
			return [self.player1, self.player2, 0]
		elif self.player1.score > self.player2.score:
			return [self.player1, self.player2]
		else:
			return [self.player2, self.player1]

	def start_game(self):
		total_account = 0
		answers = dict()
		self.code.get_test_code_text()
		self.code.bags = self.bags_list[1]
		total_errors = len(self.code.bugs)

		while total_account < total_errors:
			activ_player = self.get_activ_player()
			number = self.check_num_in_bugs()
			answer = str(input())
			if self.code.bugs[number] == answer:
				print("Правильно!")
				if (number in answers) and (answers[number] == answer):
					print("Но такой ответ уже был")
				else:
					answers[number] = answer
					activ_player.score += 1
					total_account += 1
			else:
				print("Неверно")
		winner = self.check_winner()
		if winner[-1] != 0:
			print('Победил со счетом {0}/{1} игрок - {2}'.format(winner[0].score, winner[1].score, winner[0].name))
		else:
			print('Ничья cо счетом {0}/{1}'.format(winner[0].score, winner[1].score))
		exit = input()


def main():
	Game().start_game()


if __name__ == '__main__':
	main()
