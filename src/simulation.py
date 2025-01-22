"""
Contains the main logic for the Monte Carlo simulation (game simulation, inning simulation, player stats processing).
"""

from .team import Team
from .game import simulate_game

def monte_carlo_simulation(visitor: Team, home: Team, numGames: int):
    visitor_wins = 0
    for i in range(numGames):
        result = simulate_game(visitor, home)
        if result == 'Visitor Team wins':
            visitor_wins += 1
    return visitor_wins / numGames
