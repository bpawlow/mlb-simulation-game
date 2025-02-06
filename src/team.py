"""
Define a Team class that holds information about team members, lineup, etc
"""

from .database.session import Session
from .models.team_model import TeamModel
from .player import Player

class Team:
    def __init__(self, name, lineup=None):
        self.name = name
        self.db = Session()
        
        # Try to find or create team in database
        team_model = self.db.query(TeamModel).filter_by(name=name).first()
        if not team_model:
            team_model = TeamModel(name=name)
            self.db.add(team_model)
            self.db.commit()
        
        # If lineup is provided, use it; otherwise load from database
        if lineup is not None:
            self.lineup = lineup
        else:
            self.lineup = [Player.from_model(p) for p in team_model.players]
            
    def __del__(self):
        """Close database session when object is destroyed"""
        self.db.close()

    def __repr__(self):
        lineup_players = []
        for i, player in enumerate(self.lineup):
            lineup_players.append(f"{i+1}. {player.name} - {player.positions}")
        
        return f"""Team(
            name={self.name},
            lineup={lineup_players},
        )"""
