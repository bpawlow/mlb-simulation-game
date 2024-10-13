"""
CLI Interface to run a simulated MLB game. 
"""

from src.simulation import simulate_game

if __name__ == "__main__":
    # Load teams and simulate a game
    team1 = load_team_data('data/team1.csv')
    team2 = load_team_data('data/team2.csv')
    
    result = simulate_game(team1, team2)
    print(result)