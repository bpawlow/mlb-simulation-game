"""
Define a Player class to represent each player's statistics and behavior.
"""

from .models.player_model import PlayerModel

class PlayerStats:
    def __init__(self, model_or_dict):
        if isinstance(model_or_dict, PlayerModel):
            # Initialize from database model
            self.AB = model_or_dict.ab
            self.PA = model_or_dict.pa
            self.hits = model_or_dict.hits
            self.singles = model_or_dict.singles
            self.doubles = model_or_dict.doubles
            self.triples = model_or_dict.triples
            self.home_runs = model_or_dict.home_runs
            self.strikeouts = model_or_dict.strikeouts
            self.walks = model_or_dict.walks
            self.HBP = model_or_dict.hbp
            self.FO = model_or_dict.fo
            self.GO = model_or_dict.go
            self.LO = model_or_dict.lo
            self.PO = model_or_dict.po
        else:
            # Keep existing dictionary initialization
            self.AB = model_or_dict['ab'] if 'ab' in model_or_dict else "N/A"
            self.PA = model_or_dict['pa'] if 'pa' in model_or_dict else "N/A"
            self.hits = model_or_dict['hit'] if 'hit' in model_or_dict else "N/A"
            self.singles = model_or_dict['single'] if 'single' in model_or_dict else "N/A"
            self.doubles = model_or_dict['double'] if 'double' in model_or_dict else "N/A"
            self.triples = model_or_dict['triple'] if 'triple' in model_or_dict else "N/A"
            self.home_runs = model_or_dict['home_run'] if 'home_run' in model_or_dict else "N/A"
            self.strikeouts = model_or_dict['strikeout'] if 'strikeout' in model_or_dict else "N/A"
            self.walks = model_or_dict['walk'] if 'walk' in model_or_dict else "N/A"
            self.HBP = model_or_dict['home_run'] if 'home_run' in model_or_dict else "N/A"
            self.FO = model_or_dict['b_out_fly'] if 'b_out_fly' in model_or_dict else "N/A"
            self.GO = model_or_dict['b_out_ground'] if 'b_out_ground' in model_or_dict else "N/A"
            self.LO = model_or_dict['b_out_line_drive'] if 'b_out_line_drive' in model_or_dict else "N/A"
            self.PO = model_or_dict['b_out_popup'] if 'b_out_popup' in model_or_dict else "N/A"
    
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
    def __init__(self, id, name, positions, team, year, age, stats):
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
            id=model.player_id,
            name=model.name,
            positions=model.positions.split(',') if model.positions else [],  # Convert string back to list
            team=model.team.name if model.team else None,
            year=model.year,
            age=model.age,
            stats=PlayerStats(model)
        )