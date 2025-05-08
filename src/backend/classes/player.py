"""
Define a Player class to represent each player's statistics and behavior.
"""

from dataclasses import dataclass
from typing import Optional
from ast import literal_eval
from ..models.player_model import PlayerModel

@dataclass
class PlayerStats:
    """Statistics for a player with calculated metrics.
    
    All statistics are initialized to 0 by default. Stats can be populated
    either directly or from a PlayerModel database object.
    """
    AB: int = 0
    PA: int = 0
    hits: int = 0
    singles: int = 0
    doubles: int = 0
    triples: int = 0
    home_runs: int = 0
    strikeouts: int = 0
    walks: int = 0
    HBP: int = 0
    FO: int = 0
    GO: int = 0
    LO: int = 0
    PO: int = 0
    
    @classmethod
    def from_model(cls, model: PlayerModel) -> "PlayerStats":
        """Create PlayerStats from a database model."""
        return cls(
            AB=int(model.ab) if model.ab else 0,
            PA=int(model.pa) if model.pa else 0,
            hits=int(model.hits) if model.hits else 0,
            singles=int(model.singles) if model.singles else 0,
            doubles=int(model.doubles) if model.doubles else 0,
            triples=int(model.triples) if model.triples else 0,
            home_runs=int(model.home_runs) if model.home_runs else 0,
            strikeouts=int(model.strikeouts) if model.strikeouts else 0,
            walks=int(model.walks) if model.walks else 0,
            HBP=int(model.hbp) if model.hbp else 0,
            FO=int(model.fo) if model.fo else 0,
            GO=int(model.go) if model.go else 0,
            LO=int(model.lo) if model.lo else 0,
            PO=int(model.po) if model.po else 0
        )
    
    @property
    def on_base_pct(self) -> float:
        """Calculate On-base Percentage"""
        if self.PA == 0:
            return 0.0
        return (self.hits + self.walks + self.HBP) / self.PA

    @property
    def slugging_pct(self) -> float:
        """Calculate Slugging Percentage"""
        if self.AB == 0:
            return 0.0
        return (self.singles + 2 * self.doubles + 
                3 * self.triples + 4 * self.home_runs) / self.AB

    def __repr__(self) -> str:
        """Custom representation focusing on key statistics."""
        return f"PlayerStats(obp={self.on_base_pct:.3f}, slg={self.slugging_pct:.3f})"


class Player:
    """A baseball player with their statistics and game behavior.
    
    This class represents a player and their performance statistics, handling both
    data storage and game simulation behavior. It can be initialized either directly
    or from a database model.
    
    Attributes:
        id: Unique identifier for the player
        name: Player's full name
        positions: List of positions the player can play
        team: Current team name (or None if free agent)
        year: Season year
        age: Player's age
        stats: PlayerStats object containing performance statistics
    """
    
    def __init__(
        self,
        id: str,
        name: str,
        positions: list[str],
        team: Optional[str],
        year: int,
        age: int,
        stats: dict | PlayerModel
    ):
        """Initialize a Player instance.
        
        Args:
            id: Player's unique identifier
            name: Player's full name
            positions: List of positions the player can play
            team: Team name (or None if no team)
            year: Season year
            age: Player's age
            stats: Either a dictionary of stats or a PlayerModel instance
        """
        self.id = id
        self.name = name
        self.positions = positions
        self.team = team
        self.year = year
        self.age = age
        
        # Convert stats based on input type
        if isinstance(stats, PlayerModel):
            self.stats = PlayerStats.from_model(stats)
        elif isinstance(stats, dict):
            self.stats = PlayerStats(**stats)

    @classmethod
    def from_model(cls, model: PlayerModel) -> "Player":
        """Create a Player instance from a database model.
        
        Args:
            model: PlayerModel instance from the database
            
        Returns:
            A new Player instance populated with the model's data
        """
        return cls(
            id=str(model.player_id),
            name=str(model.name),
            positions=literal_eval(str(model.positions)) if model.positions else [],
            team= None,
            year=int(model.year),
            age=int(model.age),
            stats=model  # Pass the model directly since PlayerStats handles conversion
        )
    
    def to_model(self) -> 'PlayerModel':
        """Convert Player object to PlayerModel."""
        return PlayerModel(
            player_id=self.id,
            name=self.name,
            positions=str(self.positions),
            year=self.year,
            age=self.age,
            ab=self.stats.AB,
            pa=self.stats.PA, 
            hits=self.stats.hits,
            singles=self.stats.singles,
            doubles=self.stats.doubles,
            triples=self.stats.triples,
            home_runs=self.stats.home_runs,
            strikeouts=self.stats.strikeouts,
            walks=self.stats.walks,
            hbp=self.stats.HBP,
            fo=self.stats.FO,
            go=self.stats.GO,
            lo=self.stats.LO,
            po=self.stats.PO
        )

    def __repr__(self) -> str:
        """Return a string representation of the Player."""
        return f"""Player(
            name={self.name},
            position={self.positions},
            mlb_team={self.team},
            year={self.year},
            stats={self.stats}
        )"""