"""
Contains the main logic for the Monte Carlo simulation (game simulation, inning simulation, player stats processing).
"""

from .team import Team
from .game import simulate_game

def monte_carlo_simulation(team1: Team, team2: Team, n=10000):
    team1_wins = 0
    for i in range(n):
        result = simulate_game(team1, team2)
        if result == 'Team 1 wins':
            team1_wins += 1
    return team1_wins / n


