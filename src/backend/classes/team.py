"""
Define a Team class that holds information about team members, lineup, etc
"""

from ..database.session import Session
from ..models.team_model import TeamModel
from ..models.lineup_model import LineupModel
from .player import Player
from ..models.player_model import PlayerModel

class Team:
    def __init__(self, name: str, lineup: list[tuple[Player, int, str]] | None = None, isCustom: bool = False):
        """Initialize a Team instance.
        
        Args:
            name: Team name
            lineup: Optional list of tuples containing (Player, batting_order, field_position)
            isCustom: Whether the team is a custom team
        """
        self.name = name
        self.db = Session()
        
        # Try to find or create team in database
        team_model = self.db.query(TeamModel).filter_by(name=name).first()
        if not team_model:
            team_model = TeamModel(name=name, is_mlb_team= not isCustom)
            self.db.add(team_model)
            self.db.commit()
        
        self.team_model = team_model
        
        # If lineup is provided, update database and local lineup
        if lineup is not None:
            self._update_lineup(lineup)
        
        # Load lineup from database
        self._load_lineup()
            
    def _update_lineup(self, lineup: list[tuple[Player, int, str]]) -> None:
        """Update the team's lineup in the database.
        
        Args:
            lineup: List of (Player, batting_order, field_position) tuples
        """
        # Clear existing lineup
        self.db.query(LineupModel).filter_by(team_id=self.team_model.id).delete()
        
        # Add new lineup entries
        for player, batting_order, position in lineup:
            # First check if player already exists in database
            existing_player = self.db.query(PlayerModel).filter_by(player_id=player.id).first()
            
            if not existing_player:
                # Only create new player model if it doesn't exist
                player_model = player.to_model()
                self.db.add(player_model)
            else:
                player_model = existing_player

            lineup_entry = LineupModel(
                team_id=self.team_model.id,
                player_id=player.id,
                batting_order=batting_order,
                field_position=position,
                player=player_model
            )
            self.db.add(lineup_entry)
        
        self.db.commit()
        self._load_lineup()
    
    def _load_lineup(self) -> None:
        """Load the lineup from the database into memory."""
        self.lineup = []
        for lineup_entry in self.team_model.lineup:  # Already ordered by batting_order
            player = Player.from_model(lineup_entry.player)
            self.lineup.append((player, lineup_entry.batting_order, lineup_entry.field_position))
            
    def __del__(self):
        """Close database session when object is destroyed"""
        self.db.close()

    def __repr__(self):
        lineup_players = []
        for player, batting_order, field_position in self.lineup:
            lineup_players.append(f"{batting_order}. {player.name} - {field_position}")
        
        return f"""Team(
            name={self.name},
            lineup={lineup_players},
        )"""
