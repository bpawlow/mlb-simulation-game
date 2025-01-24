"""
Simulate a game between two teams of the Teams class.
"""
from src.inning import Inning
from src.team import Team
from src.at_bat import simulate_at_bat
from typing import Literal

class Game:
    def __init__(self, visitor: Team, home: Team):
        """Initialize a new baseball game between two teams.
        
        Args:
            visitor (Team): First team in the matchup (visiting team)
            home (Team): Second team in the matchup (home team)
        """
        self.visitor = visitor
        self.home = home
        self.visitor_score = 0
        self.home_score = 0
        self.visitor_lineup_idx = 0
        self.home_lineup_idx = 0
        self.innings = 9
        self.current_inning = None
        
    def print_game_state(self, inning_num: int, half: str) -> None:
        """Print the current game state including inning and score.
        
        Args:
            inning_num (int): The current inning number
            half (str): Which half of the inning ("Top" or "Bottom")        
        """
        print(f"\n=== Inning {inning_num} {half} ===")
        print(f"Score: {self.visitor.name} {self.visitor_score}, {self.home.name} {self.home_score}")

    def play_half_inning(self, inning_num: int, half: Literal["Top", "Bottom"]) -> None:
        """Simulate one half inning of baseball.
        
        Args:
            inning_num (int): The current inning number being played
            half (Literal["Top", "Bottom"]): Which half of the inning ("Top" or "Bottom")
            
        This method simulates one half-inning of baseball by:
        1. Creating a new Inning object
        2. Printing the current game state
        3. Processing plate appearances until 3 outs are recorded
        4. Updating scores and lineup positions
        
        """
        self.current_inning = Inning(inning_num, half)
        self.print_game_state(inning_num, half)
        
        batting_team = self.visitor if half == "Top" else self.home
        lineup_idx = self.visitor_lineup_idx if half == "Top" else self.home_lineup_idx
        
        while self.current_inning.outs < 3:
            batter = batting_team.lineup[lineup_idx]
            print(f"\n{batter.name} up to bat...")
            result = simulate_at_bat(batter)
            runs = self.current_inning.process_plate_appearance(result)
            
            # Print play result
            print(f"Result: {result.name}")
            if runs > 0:
                print(f"Runs scored: {runs}")
            print(f"Outs: {self.current_inning.outs}")
            print(f"Bases: {self.current_inning.base_state.bases}")
            
            if half == "Top":
                self.visitor_score += runs
                self.visitor_lineup_idx = (lineup_idx + 1) % len(batting_team.lineup)
            else:
                self.home_score += runs
                self.home_lineup_idx = (lineup_idx + 1) % len(batting_team.lineup)
            
            lineup_idx = (lineup_idx + 1) % len(batting_team.lineup)

    def play(self) -> str:
        """Play a complete game of baseball.
        
        Returns:
            str: Result of the game ('Visitor Team wins' or 'Home Team wins')
        """
        # Play regulation innings
        for inning_num in range(1, self.innings + 1):
            # Top of inning
            self.play_half_inning(inning_num, "Top")
            
            # Check if game is over after TOP of the 9th
            if inning_num == 9 and self.home_score > self.visitor_score:
                break
                
            # Bottom of inning
            self.play_half_inning(inning_num, "Bottom")
            
            # Check if game is over after BOTTOM of the 9th
            if inning_num == 9 and self.visitor_score != self.home_score:
                break
        
        # Extra innings if tied
        extra_inning = self.innings + 1
        while self.visitor_score == self.home_score:
            self.play_half_inning(extra_inning, "Top")
            self.play_half_inning(extra_inning, "Bottom")
            extra_inning += 1
            
        # Add final score print at the end
        print(f"\nFinal Score: {self.visitor.name} {self.visitor_score}, {self.home.name} {self.home_score}")
        return "Visitor Team wins" if self.visitor_score > self.home_score else "Home Team wins"
