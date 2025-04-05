"""
Define a Player class to represent each player's statistics and behavior.
"""

from ..models.player_model import PlayerModel
from ast import literal_eval

class PlayerStats:
    def __init__(self, model_or_dict: PlayerModel | dict):
        if isinstance(model_or_dict, PlayerModel):
            # Initialize from database model, converting all values to integers
            self.AB = int(model_or_dict.ab) if model_or_dict.ab else 0
            self.PA = int(model_or_dict.pa) if model_or_dict.pa else 0
            self.hits = int(model_or_dict.hits) if model_or_dict.hits else 0
            self.singles = int(model_or_dict.singles) if model_or_dict.singles else 0
            self.doubles = int(model_or_dict.doubles) if model_or_dict.doubles else 0
            self.triples = int(model_or_dict.triples) if model_or_dict.triples else 0
            self.home_runs = int(model_or_dict.home_runs) if model_or_dict.home_runs else 0
            self.strikeouts = int(model_or_dict.strikeouts) if model_or_dict.strikeouts else 0
            self.walks = int(model_or_dict.walks) if model_or_dict.walks else 0
            self.HBP = int(model_or_dict.hbp) if model_or_dict.hbp else 0
            self.FO = int(model_or_dict.fo) if model_or_dict.fo else 0
            self.GO = int(model_or_dict.go) if model_or_dict.go else 0
            self.LO = int(model_or_dict.lo) if model_or_dict.lo else 0
            self.PO = int(model_or_dict.po) if model_or_dict.po else 0
        elif isinstance(model_or_dict, dict):
            # Initialize from dictionary, converting all values to integers
            self.AB = int(model_or_dict['ab']) if 'ab' in model_or_dict else 0
            self.PA = int(model_or_dict['pa']) if 'pa' in model_or_dict else 0
            self.hits = int(model_or_dict['hit']) if 'hit' in model_or_dict else 0
            self.singles = int(model_or_dict['single']) if 'single' in model_or_dict else 0
            self.doubles = int(model_or_dict['double']) if 'double' in model_or_dict else 0
            self.triples = int(model_or_dict['triple']) if 'triple' in model_or_dict else 0
            self.home_runs = int(model_or_dict['home_run']) if 'home_run' in model_or_dict else 0
            self.strikeouts = int(model_or_dict['strikeout']) if 'strikeout' in model_or_dict else 0
            self.walks = int(model_or_dict['walk']) if 'walk' in model_or_dict else 0
            self.HBP = int(model_or_dict['b_hit_by_pitch']) if 'b_hit_by_pitch' in model_or_dict else 0
            self.FO = int(model_or_dict['b_out_fly']) if 'b_out_fly' in model_or_dict else 0
            self.GO = int(model_or_dict['b_out_ground']) if 'b_out_ground' in model_or_dict else 0
            self.LO = int(model_or_dict['b_out_line_drive']) if 'b_out_line_drive' in model_or_dict else 0
            self.PO = int(model_or_dict['b_out_popup']) if 'b_out_popup' in model_or_dict else 0
    
    def __repr__(self):
        return f"""PlayerStats(
            obp={self.on_base_pct}, 
            slg={self.slugging_pct})"""
       
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


class Player:
    def __init__(self, id: str, name: str, positions: list[str], 
                 team: str | None, year: int, age: int, 
                 stats: dict | PlayerModel):
        self.id = id
        self.name = name
        self.positions = positions
        self.team = team
        self.year = year
        self.age = age
        self.stats = PlayerStats(stats)
        
    def __repr__(self):
        return f"""Player(
            name={self.name},
            position={self.positions},
            mlb_team={self.team},
            year={self.year},
            stats={self.stats.__repr__()}
        )"""

    @classmethod
    def from_model(cls, model: PlayerModel):
        """Create a Player instance from a database model.
        
        This is a class method that takes a PlayerModel database object and converts it into a Player instance.
        It extracts the player's information from the database model including:
        - player_id: The unique identifier for the player
        - name: The player's name
        - positions: What positions they play
        - team: The name of their MLB team (or None if no team)
        - year: The season year
        - age: Player's age
        - stats: Their statistics wrapped in a PlayerStats object
        
        Args:
            model (PlayerModel): The database model containing player data
            
        Returns:
            Player: A new Player instance populated with the model's data
        """
        return cls(
            id=str(model.player_id),
            name=str(model.name),
            positions=literal_eval(str(model.positions)) if model.positions else [],
            team=model.team.name if model.team else None,
            year=int(model.year),
            age=int(model.age),
            stats=model  # Pass the model directly since PlayerStats handles conversion
        )