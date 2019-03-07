
class Automat:
	tranzitii = []

	def __init__(self, name):
		self.read_data(name)
	
	def read_data(self, filename):
		with open(filename, 'r') as f:
			self.nr_stari = int(f.readline())
			self.stare_init = int(f.readline())
			self.stari_finale = [int(i) for i in f.readline().split(" ")]
			for line in f:
				components = line.split(" ")
				start =	int(components[0])
				finish = int(components[1])
				litera = components[2].strip()
				t = Tranzitie(start, finish, litera)
				self.tranzitii.append(t)

	def check_word(self, word, stare_curenta):			#functie recursiva care verifica daca un cuvant este valid
		if not word:
			if stare_curenta in self.stari_finale:
				return True
			else:
				return False

		trans_list = self.available_transitions(stare_curenta)
		for trans in trans_list:
			if trans.litera == word[0]:
				stare_curenta = trans.finish
				return self.check_word(word[1:], stare_curenta)


	def available_transitions(self, stare):		#functie care calculeaza tranzitiile valabile dintr-o stare data
		trans_list = []
		for t in self.tranzitii:
			if t.start == stare:
				trans_list.append(t)
		return trans_list


class Tranzitie:
	def __init__(self, start, finish, litera):
		self.start = start
		self.finish = finish
		self.litera = litera



cuvinte = ["", "aaaa", "bbabaaa", "aabbbabaab", "abbabb"]
a = Automat("read.txt")
for cuv in cuvinte:
	print("Cuvantul " + cuv + " este valid pentru automat: ")
	print(a.check_word(cuv, a.stare_init))
