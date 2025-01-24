"""
Logic for base running, including runner advancement and scoring.
"""

from src.hit_outcomes import HitType, OutType
from random import random

class BaseState:
    def __init__(self):
        self.bases = [False, False, False]  # First, Second, Third
        self.runners_on_base = sum(1 for base in self.bases if base)
        self.runs_scored = 0
        self.was_double_play = False
        
    def count_scored_baserunners(self, start_base: int = 0) -> int:
        """Count number of runners from a given base position onwards.
        
        Args:
            start_base (int): Starting base index (0=first, 1=second, 2=third)
        Returns:
            int: Number of runners on the specified bases
        """
        return sum(1 for base in self.bases[start_base:] if base)
    
    def advance_runners(self, bat_result: HitType | OutType, outs: int) -> int:
        """Advance runners and calculate runs scored based on the hit type and number of outs.
        
        Args:
            bat_result (HitType | OutType): The type of hit or out that occurred
            outs (int): The number of outs before this play
            
        Returns:
            int: Number of runs scored on this play
            
        The function handles all types of hits (singles, doubles, triples, home runs) 
        and outs (fly balls, ground outs, etc.) according to standard baseball rules.
        For hits, runners advance the appropriate number of bases based on the hit type.
        For outs, runners may advance on sacrifice flies or force plays.
        """
        runs = 0
        self.was_double_play = False  # Reset the flag at the start of each play
        
        if isinstance(bat_result, HitType):
            # Handle hits
            if bat_result == HitType.HOME_RUN:
                # Score all runners plus batter
                runs = self.count_scored_baserunners() + 1
                self.bases = [False, False, False]
                
            elif bat_result == HitType.TRIPLE:
                # Score all runners, put batter on third
                runs = self.count_scored_baserunners()
                self.bases = [False, False, True]
                
            elif bat_result == HitType.LONG_DOUBLE:
                # Score from first, second, and third, batter to second
                runs = self.count_scored_baserunners()
                self.bases = [False, True, False]
                
            elif bat_result == HitType.SHORT_DOUBLE:
                # Score from second and third, batter to second
                runs = self.count_scored_baserunners(1)
                self.bases = [False, True, False]
                
            elif bat_result == HitType.LONG_SINGLE:
                # Advance all runners 2 bases, batter to first
                runs = self.count_scored_baserunners(1)
                self.bases = [True, False, self.bases[0]]
                
            elif bat_result == HitType.MEDIUM_SINGLE:
                # Score from second, advance others one base
                runs = self.count_scored_baserunners(1)
                self.bases = [True, self.bases[0], self.bases[1]]
                
            elif bat_result in (HitType.SHORT_SINGLE, HitType.ERROR):
                # Advance all runners one base
                runs = self.count_scored_baserunners(2)
                self.bases = [True, self.bases[0], self.bases[1]]
                
            elif bat_result in (HitType.WALK, HitType.HBP):
                # Advance runners only if forced
                if all(self.bases):
                    runs += 1
                for i in range(2, -1, -1):
                    if all(self.bases[:i+1]):
                        self.bases[i] = True
                self.bases[0] = True
                
        elif isinstance(bat_result, OutType):
            # Handle outs
            if bat_result == OutType.MEDIUM_FLY and outs < 2:
                # Score from third on sac fly
                if self.bases[2]:
                    runs += 1
                    self.bases[2] = False
                    
            elif bat_result == OutType.LONG_FLY and outs < 2:
                # Advance runner from second or third
                if self.bases[2]:
                    runs += 1
                    self.bases[2] = False
                elif self.bases[1]:
                    self.bases[1] = False 
                    self.bases[2] = True
                    
            elif bat_result == OutType.GROUND_OUT:
                # Handle ground out differently based on base state
                if self.bases[0]:  # Runner on first
                    # 50% chance of double play if less than 2 outs
                    if outs < 2 and random() < 0.5:
                        self.was_double_play = True # Set the flag
                        # Double play - force at second, batter out at first
                        self.bases[0] = False
                        if self.bases[2]:  # Runner on third scores
                            runs += 1
                        self.bases[2] = self.bases[1]
                        self.bases[1] = False
                    else:
                        # Regular force out - advance all runners one base
                        if self.bases[2]:
                            runs += 1
                        self.bases[2] = self.bases[1]
                        self.bases[1] = self.bases[0]
                        self.bases[0] = False
                else:
                    # No runner on first - regular ground out
                    if self.bases[2]:  # Runner on third scores
                        runs += 1
                    if self.bases[1]:  # Runner on second advances to third
                        self.bases[2] = True
                        self.bases[1] = False
                    self.bases[0] = False
                
        self.runs_scored += runs
        return runs
    def __repr__(self):
        return f"Bases: {self.bases}, Runs: {self.runs}"