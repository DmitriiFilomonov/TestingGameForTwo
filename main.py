from random import randint


class Code(object):
	def __init__(self, text_code = ["abcd = 666", "prints(abcd)"], bugs = {1: "abcd = int(666)", 2: "print(abcd)"}):
		self.text_code = text_code
		self.bugs = bugs

	def get_test_code_text(self, num):
		i = 1
		text_code_file = open("text_code"+str(num)+".txt", "r")
		print()
		for line in text_code_file:
			print(i, line)
			self.text_code.append(line)
			i += 1
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
		self.bugs_list = {1: {2:"    if n <= 1:", 
					 6:"        for i in range(1, n):", 
					 7: "            m, k = k, (m+k)%10", 
					 13: "    print(fib_digit(n))", 
					 16:'''if __name__ == "__main__":''',
					 17: "    main()"},
				 2: {2:"    if n == 0:", 
					 4:"    else:", 
					 6: "        for i in range(2, n+1):"},
				 3: {5:"        return pass", 
					 8:"        return pass", 
					 11: "    for i in range(m*6):", 
					 13: "        pis.append(n1%m)", 
					 16:'''            break'''}}

	def set_players(self, name1, name2):
		self.player1.name = name1
		self.player2.name = name2

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
		print("Игра в тестирование программ (для 2 игроков)")
		print("Игроки по очереди указывают номер строки и код, который они считают правильным")
		print("Побеждает тот игрок, который получил больше баллов за правильные ответы")
		print()
		total_account = 0
		answers = dict()

		name1 = str(input("Представьтесь игрок №1 - "))
		name2 = str(input("Представьтесь игрок №2 - "))
		self.set_players(name1, name2)
		print("Ниже представлен код, в котором вы должны найти ошибки")
		num = randint(1, 3)
		self.code.get_test_code_text(num)
		self.code.bugs = self.bugs_list[num]
		total_errors = len(self.code.bugs)
		while total_account < total_errors:
			activ_player = self.get_activ_player()
			number = self.check_num_in_bugs()
			print("Исправьте указанную строку учитывая все отступы")
			answer = str(input())
			if number in self.code.bugs and self.code.bugs[number] == answer:
				print("Правильно!")
				if (number in answers) and (answers[number] == answer):
					print("Но такой ответ уже был")
				else:
					f = input("f")
					answers[number] = answer
					activ_player.score += 1
					total_account += 1
			else:
				f = input("f")
				print("Неверно")
		print("Игра окончена")
		winner = self.check_winner()
		if winner[-1] != 0:
			print('Победил со счетом {0}/{1} игрок - {2}'.format(winner[0].score, winner[1].score, winner[0].name))
		else:
			print('Ничья cо счетом {0}/{1}'.format(winner[0].score, winner[1].score))
		exit = input("Нажмите клавишу Enter для завершения")


def main():
	Game().start_game()


if __name__ == '__main__':
	main()
