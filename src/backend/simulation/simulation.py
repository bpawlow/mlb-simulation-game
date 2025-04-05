"""
Contains the main logic for the Monte Carlo simulation (game simulation, inning simulation, player stats processing).
"""

from ..classes.team import Team
from ..game.game import Game

def monte_carlo_simulation(visitor: Team, home: Team, numGames: int):
    visitor_wins = 0
    for i in range(numGames):
        # Create game and run simulation
        game = Game(visitor, home)
        result = game.play()
        print(result)
    return visitor_wins / numGames
