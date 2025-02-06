from enum import Enum, auto

class HitType(Enum):
    """Enum representing different types of hits and their base-running outcomes.
    
    Each enum value represents a different type of hit or positive batting outcome,
    with specific rules for how baserunners advance.
    """
    SHORT_SINGLE = auto()  # Batter to first, runners advance one base
    MEDIUM_SINGLE = auto() # Batter to first, scores from second, first to second
    LONG_SINGLE = auto()   # Batter to first, all runners advance two bases
    SHORT_DOUBLE = auto()  # Batter to second, runners advance two bases
    LONG_DOUBLE = auto()   # Batter to second, scores runner from first
    TRIPLE = auto()        # Batter to third, all runners score
    HOME_RUN = auto()      # Batter and all runners score
    ERROR = auto()         # Batter reaches 1st on error, runners advance one base
    WALK = auto()          # Batter to first, runners advance if forced
    HBP = auto()          # Hit by pitch, same rules as walk


class OutType(Enum):
    """Enum representing different types of outs and their base-running outcomes.
    
    Each enum value represents a different way a batter can make an out,
    with specific rules for how baserunners may advance with less than 2 outs.
    """
    STRIKE_OUT = auto()    # Batter strikes out, no runner advancement
    GROUND_OUT = auto()    # Ground out with force play potential and runner advancement
    POP_OUT = auto()       # Infield pop out, no runner advancement
    LINE_OUT = auto()      # Line out, no runner advancement
    SHORT_FLY = auto()     # Short fly out, no runner advancement
    MEDIUM_FLY = auto()    # Medium fly out, runner on third may score
    LONG_FLY = auto()      # Deep fly out, runners on second/third may advance