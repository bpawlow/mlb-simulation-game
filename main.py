"""
CLI Interface to run a simulated MLB game. 
"""

from src.game import Game
from data.process_data import process_data
from src.utils import create_test_teams_matchup
import pandas as pd

if __name__ == "__main__":
    # Load teams
    players_df = pd.read_csv('data/players.csv')
    
    # Create two teams to simulate a game (Example)
    team1, team2 = create_test_teams_matchup(players_df)
    
    # Create Team objects from processed player data
    # teams = create_team_objects(players_df)
    
    # Create game and run the simulation
    game = Game(team1, team2)
    result = game.play()