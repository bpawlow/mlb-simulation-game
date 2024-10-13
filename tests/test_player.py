"""
Unit tests for Player class.
"""

import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_stats(self):
        player = Player("John Doe", 0.300, 0.450)
        self.assertEqual(player.batting_avg, 0.300)