"""
Logic to simulate the outcome of an at-bat, given player statistics.
"""

import random
from .hit_outcomes import HitType, OutType 
from ..classes.player import Player
from typing import Dict

def simulate_at_bat(player: Player) -> HitType | OutType:
    roll = random.random()
    
    # Check for walk or HBP first
    if roll < player.stats.walks / player.stats.PA:
        return HitType.WALK
    elif roll < (player.stats.walks + player.stats.HBP) / player.stats.PA:
        return HitType.HBP
    
    # Check for hits
    if roll < player.stats.on_base_pct:
        # Calculate proportions of different hit types
        total_hits = player.stats.hits
        hit_distribution = {
            HitType.HOME_RUN: player.stats.home_runs / total_hits,
            HitType.TRIPLE: player.stats.triples / total_hits,
            HitType.ERROR: 0.02, #estimating error frequency to be about 2% of the time
            HitType.LONG_DOUBLE: (player.stats.doubles * 0.2) / total_hits,  # Estimating 20% are long doubles
            HitType.SHORT_DOUBLE: (player.stats.doubles * 0.8) / total_hits, # Estimating 80% are short doubles
            HitType.LONG_SINGLE: (player.stats.singles * 0.3) / total_hits,  # Estimating 30% are long singles
            HitType.MEDIUM_SINGLE: (player.stats.singles * 0.5) / total_hits,# Estimating 50% are medium singles
            HitType.SHORT_SINGLE: (player.stats.singles * 0.2) / total_hits  # Estimating 20% are short singles
        }
        return weighted_random_choice(hit_distribution)
    
    # It's an out
    out_distribution = {
        OutType.STRIKE_OUT: player.stats.strikeouts / player.stats.PA,
        OutType.GROUND_OUT: player.stats.GO / player.stats.PA,
        OutType.POP_OUT: player.stats.PO / player.stats.PA,
        OutType.LINE_OUT: player.stats.LO / player.stats.PA,
        # Split remaining outs between short, medium, and long fly balls
        OutType.SHORT_FLY: (player.stats.FO * 0.2) / player.stats.PA,
        OutType.MEDIUM_FLY: (player.stats.FO * 0.5) / player.stats.PA,
        OutType.LONG_FLY: (player.stats.FO * 0.3) / player.stats.PA
    }
    return weighted_random_choice(out_distribution)

def weighted_random_choice(distribution: Dict[HitType, float] | Dict[OutType, float]):
    """Helper function to choose from a weighted distribution"""
    
     # Calculate total probability
    total_prob = sum(distribution.values())
    if total_prob == 0:
        raise ValueError("All probabilities are zero")
    
    # Normalize the roll to the total probability
    roll = random.random() * total_prob
    
    cumulative = 0
    for outcome, probability in distribution.items():
        cumulative += probability
        if roll < cumulative:
            return outcome

    # This should never happen now that we've normalized the roll
    raise RuntimeError("Failed to select an outcome - this shouldn't happen")


