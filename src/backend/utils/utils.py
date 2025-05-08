"""
Helper functions such as data loading/modeling, randomization, or utility methods for simulations.
"""

import pandas as pd
from ..classes.team import Team
from ..classes.player import Player
from typing import Dict

def create_test_teams_matchup() -> tuple[Team, Team]:
    """Create two test teams with balanced lineups from a pool of players.
    
    Creates two teams by selecting players from the database, ensuring each team
    has players for each position and no duplicate players between teams.
        
    Returns:
        tuple: A tuple containing two Team objects with balanced lineups
    """
    from ..database.session import Session
    from ..models.player_model import PlayerModel
    
    # Initialize database session
    db = Session()
    
    # Get all players from database
    all_players = db.query(PlayerModel).all()
    
    # Required positions for a complete lineup
    positions = ['C', '1B', '2B', '3B', 'SS', 'OF', 'OF', 'OF']  # DH will be assigned from remaining players
    
    # Initialize teams
    teams = []
    team_names = ['Team A', 'Team B']
    
    # Create two teams
    used_players = set()
    for team_name in team_names:
        lineup = []
        # Fill each position
        for batting_order, position in enumerate(positions, 1):
            # Find first available player that can play this position
            for player_model in all_players:
                player_positions = eval(player_model.positions)
                if position in player_positions and player_model.player_id not in used_players:
                    # Convert PlayerModel to Player object
                    player = Player.from_model(player_model)
                    lineup.append((player, batting_order, position))
                    used_players.add(player_model.player_id)
                    break
        
        # Add DH as 9th batter from remaining players
        for player_model in all_players:
            if player_model.player_id not in used_players:
                player = Player.from_model(player_model)
                lineup.append((player, 9, 'DH'))
                used_players.add(player_model.player_id)
                break
                
        teams.append(Team(team_name, lineup, isCustom=True))
    
    db.close()
    return teams[0], teams[1]