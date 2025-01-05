"""
CLI Interface to run a simulated MLB game. 
"""

from src.simulation import simulate_game
from data.process_data import process_data
from src.utils import create_test_teams_matchup

if __name__ == "__main__":
    # Load teams and process data
    players_df = process_data('data/hitting-stats.csv', 'data/player-positions.csv', 'data/players.csv')
    
    # Create two teams to simulate a game (Example)
    team1, team2 = create_test_teams_matchup(players_df)
    
    # Create Team objects from processed player data
    # teams = create_team_objects(players_df)
    
    # Run the simulation
    result = simulate_game(team1, team2)
    
    print('Team 1: ', team1)
    print('Team 2: ', team2)