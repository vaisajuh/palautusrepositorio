import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.kauppa = Mock()
        self.saldot = {1:1, 2:2}
        self.alustetaan_kauppa_ja_tuotteet()

    def alustetaan_kauppa_ja_tuotteet(self):
  
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return self.saldot[1]
            
            if tuote_id == 2:
                return self.saldot[2]

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "kala", 10)

        def varasto_ota_varastosta(tuote):
            if tuote.id == 1:
                self.saldot[1] = varasto_saldo(1) - 1
            if tuote.id == 2:
                self.saldot[2] = varasto_saldo(2) - 1

        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.varasto_mock.ota_varastosta.side_effect = varasto_ota_varastosta
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
            
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_lisataan_koriin_yksi_tuote(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)
    
    def test_lisataan_koriin_kaksi_tuotetta(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 15)
    
    def test_kaksi_samaa_tuotetta_joita_on_tarpeeksi(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)
    
    def test_tarpeeksi_ja_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 15)
    
    def test_nollaa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 10)