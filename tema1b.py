class Tranzitie:
    def __init__(self, start, finish, litera):
        self.start = start
        self.finish = finish
        self.litera = litera


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
                start = int(components[0])
                finish = int(components[1])
                litera = components[2].strip()
                t = Tranzitie(start, finish, litera)
                self.tranzitii.append(t)


    def check_word(self, word, stari_curente):  # functie recursiva care verifica daca un cuvant este valid
        if not isinstance(stari_curente, list):
            stari_curente = [stari_curente]     #cand vectorul are un singur element, python nu il recunoaste ca vector

        if not word:
            if any(s in stari_curente for s in self.stari_finale):
                return True
            else:
                return False

        trans_list = self.available_transitions(stari_curente)
        stari_posibile =[]
        for trans in trans_list:
            if trans.litera == word[0]:
                stari_posibile.append(trans.finish)

        if not stari_posibile:
            return False
        else:
            return self.check_word(word[1:], stari_posibile)


    def available_transitions(self, stari):  # functie care calculeaza tranzitiile valabile din niste stari date
        trans_list = []
        for t in self.tranzitii:
            if t.start in stari:
                trans_list.append(t)
        return trans_list




cuvinte = ["abaa", "", "bba", "bbaa"]
a = Automat("read.txt")
for cuv in cuvinte:
    print("Cuvantul " + cuv + " este valid pentru automat: ")
    print(a.check_word(cuv, a.stare_init))
