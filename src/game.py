"""
Simulate a game between two teams of the Teams class.
"""
from .team import Team
from .inning import simulate_inning
from .at_bat import simulate_at_bat
from .hit_outcomes import HitType, OutType

def simulate_game(visitor: Team, home: Team) -> str:
    """Simulates a single baseball game between two teams.
    
    Args:
        visitor (Team): First team in the matchup
        home (Team): Second team in the matchup
        
    Returns:
        str: Result of the game ('Visitor Team wins' or 'Home Team wins')
    """
    # Initialize game state
    visitor_score = 0
    home_score = 0
    innings = 9
    
    # Track batting order position for each team
    visitor_lineup_idx = 0
    home_lineup_idx = 0
    
    # Simulate each inning
    for inning in range(1, innings):
        # Top of inning - Visitor Team bats
        outs = 0
        while outs < 3:
            batter = visitor.lineup[visitor_lineup_idx]
            result = simulate_at_bat(batter)
            
            # 
            # TODO Implement base running logic
            #
            
            # 
            # TODO Increment runs and/or outs based on base running calculations
            #
                
            # Advance to next batter, wrapping around lineup
            visitor_lineup_idx = (visitor_lineup_idx + 1) % len(visitor.lineup)
            
        # Check if game is over after TOP of the 9th inning
        if inning == 9 and home_score > visitor_score:
            break
            
        # Bottom of inning - Home Team bats
        outs = 0
        while outs < 3:
            batter = home.lineup[home_lineup_idx]
            result = simulate_at_bat(batter)
            
            # 
            # TODO Implement base running logic
            #
            
            # 
            # TODO Increment runs and/or outs based on base running calculations
            #
                
            home_lineup_idx = (home_lineup_idx + 1) % len(home.lineup)
            
        # Check if game is over after BOTTOM of the 9th inning
        if inning == 9 and visitor_score != home_score:
            break
            
    # Extra innings if tied
    while visitor_score == home_score:
        # Top of inningf
        outs = 0
        while outs < 3:
            batter = visitor.lineup[visitor_batter_idx]
            result = simulate_at_bat(batter)
            if result == "out":
                outs += 1
            else:
                visitor_score += 1
            visitor_batter_idx = (visitor_batter_idx + 1) % len(visitor.lineup)
            
        # Bottom of inning    
        outs = 0
        while outs < 3:
            batter = home.lineup[home_batter_idx]
            result = simulate_at_bat(batter)
            if result == "out":
                outs += 1
            else:
                home_score += 1
            home_batter_idx = (home_batter_idx + 1) % len(home.lineup)
            
    return "Visitor Team wins" if visitor_score > home_score else "Home Team wins"


