"""
Helper functions such as data loading/modeling, randomization, or utility methods for simulations.
"""

import pandas as pd
from ..classes.team import Team
from ..classes.player import Player
from typing import List, Dict

def create_test_teams_matchup(players_df: pd.DataFrame) -> List[Team]:
    """Create two test teams with balanced lineups from a pool of players.
    
    Creates two teams by selecting players from the provided DataFrame, ensuring each team
    has players for each position and filling remaining spots with designated hitters.
    
    Args:
        players_df (pandas.DataFrame): DataFrame containing available players and their stats
        
    Returns:
        tuple: A tuple containing two Team objects (team1, team2) ready for simulation
    """
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
            for j in range(9-len(team_players)):
                dh_player = available_players.iloc[0]
                team_players.append(dh_player)
                # Remove selected player from available pool
                available_players = available_players[available_players.player_id != dh_player.player_id]
        
        # Convert team_players list to DataFrame
        team_df = pd.DataFrame(team_players)
        # Create lineup and team object
        lineup = create_player_objects(team_df)
        teams.append(Team(team_names[i], lineup))
    
    return teams


def create_team_objects(players_df: pd.DataFrame) -> Dict[str, Team]:
    """Create Team objects from processed player data, grouped by team.
    
    Args:
        players_df (pandas.DataFrame): DataFrame containing player data with team assignments
        
    Returns:
        dict: Dictionary mapping team names to Team objects containing their lineups
    """
    # Group players by team
    teams = {}
    
    for team_name, team_players in players_df.groupby('team'):
        lineup = create_player_objects(team_players)
        # Create Team object with lineup
        teams[team_name] = Team(str(team_name), lineup)
        
    return teams


def create_player_objects(team_players: pd.DataFrame) -> List[Player]:
    """Create Player objects from processed player data for a specific team.
    
    Args:
        team_name (str): Name of the team these players belong to
        team_players (pandas.DataFrame): DataFrame containing player data for a single team
        
    Returns:
        list: List of Player objects representing the team's lineup
    """
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