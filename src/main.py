"""
CLI Interface to run a simulated MLB game. 
"""

from backend.database.setup_db import setup_database
from backend.game.game import Game
from backend.classes.team import Team
from backend.utils.utils import create_test_teams_matchup

if __name__ == "__main__":
    # Initialize and populate database
    setup_database()
    
    # Create teams using database data
    team1, team2 = create_test_teams_matchup()
    
    # Create game and run simulation
    game = Game(team1, team2)
    result = game.play()
    print(result)