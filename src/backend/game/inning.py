"""
Represents a single inning in a baseball game, tracking outs, base runners, and scoring.

This module provides the Inning class which handles the state and logic for one
half-inning of baseball, including tracking outs, managing baserunners, and 
calculating runs scored.
"""

from .hit_outcomes import HitType, OutType
from .base_running import BaseState
from typing import Literal

class Inning:
    """A class representing one half-inning of a baseball game.
    
    This class maintains the state of an inning including number of outs,
    base runners, and handles the logic for processing plate appearances.
    
    Attributes:
        number (int): The inning number (1-9 or more for extra innings)
        half (Literal["Top", "Bottom"]): Which half of the inning ("Top" or "Bottom")
        outs (int): Number of outs in the current inning (0-3)
        base_state (BaseState): Object tracking runners on base
    """

    def __init__(self, number: int, half: Literal["Top", "Bottom"]):
        self.number = number
        self.half = half
        self.outs = 0
        self.base_state = BaseState()

    def process_plate_appearance(self, bat_result: HitType | OutType) -> int:
        """Process a plate appearance and return runs scored on the play.
        
        Handles the result of a plate appearance by:
        1. Advancing runners and calculating runs scored
        2. Updating number of outs if the result was an out
        3. Handling special cases like double plays
        
        Args:
            bat_result (HitType | OutType): The result of the plate appearance
            
        Returns:
            int: Number of runs scored on the play
        """
        runs = self.base_state.advance_runners(bat_result, self.outs)
        
        # Update outs if the result was an out
        if isinstance(bat_result, OutType):
            # whether it was a double play
            self.outs += 2 if self.base_state.was_double_play else 1
                
        return runs

    def __repr__(self):
        """Return string representation of the inning state."""
        return f"Inning {self.number} ({self.half}): Outs: {self.outs}, {self.base_state}"