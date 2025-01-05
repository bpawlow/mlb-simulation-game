"""
Define a Team class that holds information about team members, lineup, etc
"""

class Team:
    def __init__(self, name, lineup):
        self.name = name
        self.lineup = lineup  # List of Player objects
        
    def __repr__(self):
        lineup_players = []
        for i, player in enumerate(self.lineup):
            lineup_players.append(f"{i+1}. {player.name} - {player.positions}")
        
        return f"""Team(
            name={self.name},
            lineup={lineup_players},
        )"""
