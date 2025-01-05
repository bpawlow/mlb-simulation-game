"""
Logic to simulate the outcome of an at-bat, given player statistics.
"""

import random

def simulate_at_bat(player, outcome_probabilities):
    # First determine if it's a hit, walk, or out
    roll = random.random()
    
    if roll < player.stats['walk_rate']:
        return HitType.WALK
    
    if roll < player.stats['on_base_pct']:
        # Determine hit type based on slugging percentage
        return determine_hit_type(player, outcome_probabilities['hit'])
    
    # It's an out
    return determine_out_type(player, outcome_probabilities['out'])

def determine_hit_type(player, hit_probabilities):
    pass

def determine_out_type(player, out_probabilities):
    pass    



