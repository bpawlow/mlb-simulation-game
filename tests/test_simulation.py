"""
Unit tests for simulate game logic.
"""

import unittest
from src.simulation import simulate_game

class TestSimulation(unittest.TestCase):
    def test_simulate_game(self):
        result = simulate_game(team1, team2)
        self.assertIn(result, ['Team 1 wins', 'Team 2 wins'])