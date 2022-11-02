import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
            self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search(self):
        semenko = self.statistics.search("Semenko")
        self.assertEqual(semenko.name, "Semenko")
        not_semenko = self.statistics.search("emkrere")
        self.assertEqual(not_semenko, None)
    
    def test_team(self):
        semenko = self.statistics.team("EDM")
        self.assertEqual(semenko[0].name, "Semenko")
    
    def test_top(self):
        gretzky = self.statistics.top(1)
        self.assertEqual(gretzky[0].name, "Gretzky")
