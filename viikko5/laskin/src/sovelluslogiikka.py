class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        miinus = self.tulos - arvo
        return miinus

    def plus(self, arvo):
        summa = self.tulos + arvo
        return summa

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
