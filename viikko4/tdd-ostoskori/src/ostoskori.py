from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maarat = map(lambda m: m.lukumaara(), self.kori)
        return sum(maarat)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinnat = map(lambda h: h.hinta(), self.kori)
        return sum(hinnat)
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        olio = Ostos(lisattava)
        count = 0
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == olio.tuotteen_nimi():
                count += 1
                ostos.muuta_lukumaaraa(1)
        if count == 1:
            return
        self.kori.append(olio)


    def poista_tuote(self, poistettava: Tuote):
        olio = Ostos(poistettava)
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == olio.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.kori.remove(ostos)

    def tyhjenna(self):
        self.kori.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
