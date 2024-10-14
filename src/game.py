"""
Simulate a game between two teams of the Teams class.
"""
from .team import Team
from .inning import simulate_inning

def simulate_game(team1: Team, team2: Team):
    # Monte Carlo logic to simulate innings and calculate score
    team1_score = 0
    team2_score = 0
    for inning in range(9):
        team1_score += simulate_inning(team1['lineup'])
        team2_score += simulate_inning(team2['lineup'])
    return 'Team 1 wins' if team1_score > team2_score else 'Team 2 wins'
