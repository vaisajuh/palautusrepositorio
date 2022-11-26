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
        if olio in self.kori:
            self.poista_tuote(lisattava)
            olio.lukumaara += 1
            self.kori.append(olio)
        else:
            self.kori.append(olio)

    def poista_tuote(self, poistettava: Tuote):
        olio = Ostos(poistettava)
        self.kori = list(
            filter(lambda t: olio.tuoteen_nimi != self.kori)
        )

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
