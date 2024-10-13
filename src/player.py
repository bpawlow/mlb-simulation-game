"""
Define a Player class to represent each player’s statistics and behavior.
"""

class Player:
    def __init__(self, name, batting_avg, slugging_pct):
        self.name = name
        self.batting_avg = batting_avg
        self.slugging_pct = slugging_pct