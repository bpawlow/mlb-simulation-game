"""
Define a Player class to represent each player’s statistics and behavior.
"""

class PlayerStats:
    def __init__(self, stats):
        self.AB = stats['ab'] if 'ab' in stats else "N/A"
        self.PA = stats['pa'] if 'pa' in stats else "N/A"
        self.hits = stats['hit'] if 'hit' in stats else "N/A"
        self.singles = stats['single'] if 'single' in stats else "N/A"
        self.doubles = stats['double'] if 'double' in stats else "N/A"
        self.triples = stats['triple'] if 'triple' in stats else "N/A"
        self.home_runs = stats['home_run'] if 'home_run' in stats else "N/A"
        self.strikeouts = stats['strikeout'] if 'strikeout' in stats else "N/A"
        self.walks = stats['walk'] if 'walk' in stats else "N/A"
        self.HBP = stats['home_run'] if 'home_run' in stats else "N/A"
        self.FO = stats['b_out_fly'] if 'b_out_fly' in stats else "N/A"
        self.GO = stats['b_out_ground'] if 'b_out_ground' in stats else "N/A"
        self.LO = stats['b_out_line_drive'] if 'b_out_line_drive' in stats else "N/A"
        self.PO = stats['b_out_popup'] if 'b_out_popup' in stats else "N/A"
        self.ROE = stats['b_reached_on_error'] if 'b_reached_on_error' in stats else "N/A"
    
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