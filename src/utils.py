"""
Helper functions such as data loading/modeling, randomization, or utility methods for simulations.
"""

import pandas as pd
from src.team import Team
from src.player import Player, PlayerStats

# Load processed player data
def load_player_data(file_path): 
    pass 
    

# Create 2 example teams to play each other
def create_test_teams_matchup(players_df):
    # Initialize empty teams list
    teams = []
    team_names = ['Team A', 'Team B']
    
    # Create a copy of the player pool to remove selected players
    available_players = players_df.copy()
    
    for i in range(2):
        team_players = []
        # Get primary position for each player (first position in list)
        available_players['primary_position'] = available_players['position'].apply(lambda x: x[0])
        # Group available players by position
        for position, pos_group in available_players.groupby('primary_position'):
            # Select first available player for this position
            if len(pos_group) > 0:
                selected_player = pos_group.iloc[0]
                team_players.append(selected_player)
                # Remove selected player from available pool
                available_players = available_players[available_players.player_id != selected_player.player_id]
        
        #Add DH to lineup if needed
        if len(team_players) < 9:
            for i in range(9-len(team_players)):
                dh_player = available_players.iloc[0]
                team_players.append(dh_player)
                # Remove selected player from available pool
                available_players = available_players[available_players.player_id != dh_player.player_id]
        
        # Convert team_players list to DataFrame
        team_df = pd.DataFrame(team_players)
        # Create lineup and team object
        lineup = create_player_objects(team_names[i], team_df)
        teams.append(Team(team_names[i], lineup))
    
    return teams

      
# Create Team objects from processed player data
def create_team_objects(players_df):
     # Group players by team
    teams = {}
    
    for team_name, team_players in players_df.groupby('team'):
        lineup = create_player_objects(team_name,team_players)
        # Create Team object with lineup
        teams[team_name] = Team(team_name, lineup)
        
    return teams
    

# Create Player objects from processed player data
def create_player_objects(team_name, team_players):
    
    # Convert each player row into a dict of stats
    lineup = []
    for _, player in team_players.iterrows():
        
         # Get all hitting stats as a dictionary
        stats = player.loc["player_age":].to_dict()
        
        new_player = Player(
            id=player["player_id"],
            name=player["name"],
            positions=player["position"],
            team=player["team"],
            year=player["year"],
            age=player["player_age"],
            stats=stats
        )
        lineup.append(new_player)
        
    return lineup
            
       