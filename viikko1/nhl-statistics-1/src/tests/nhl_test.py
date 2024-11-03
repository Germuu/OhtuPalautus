import unittest
from statistics_service import StatisticsService
from statistics_service import SortBy
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_found(self):
        self.assertEqual(self.stats.search("Gretzky"), self.stats._players[-1])
    
    def test_search_not_found(self):
        self.assertEqual(self.stats.search("Moritz"), None)
        
    def test_team(self):
        self.assertEqual(self.stats.team("PIT")[0], self.stats._players[1])
    
    def test_top_points(self):
        self.assertEqual(self.stats.top(1)[0], self.stats._players[-1])

    def test_top_goals(self):
        self.assertEqual(self.stats.top(1, SortBy.GOALS)[0],self.stats._players[1] )

    def test_top_assists(self):
        self.assertEqual(self.stats.top(1, SortBy.ASSISTS)[1],self.stats._players[3] )   

