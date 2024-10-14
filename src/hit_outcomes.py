from enum import Enum, auto

class HitType(Enum):
    SHORT_SINGLE = auto() #advances one base
    MEDIUM_SINGLE = auto() #scores from 2nd
    LONG_SINGLE = auto() #advances 2 bases
    SHORT_DOUBLE = auto() #runners advance 2 bases
    LONG_DOUBLE = auto() #scores a runner from 1st
    TRIPLE = auto()
    HOME_RUN = auto()
    ERROR = auto()
    SACRIFICE = auto()
    WALK = auto()
    HBP = auto()


class OutType(Enum):
    STRIKE_OUT = auto()
    FLY_OUT = auto()
    GROUND_OUT = auto() # force out for a runner if possible. 2nd -> 3rd and 3rd -> Home advances.
    GIDP = auto() #ground into double play
    LDIF = auto() #line drive or infield fly
    SHORT_FLY = auto() #does not advance any runners 
    MEDIUM_FLY = auto() #(if fewers than 2 outs) scores a runner from third
    LONG_FLY = auto() #(if fewer than 2 outs) advances a runner on second or third one base
    
    
    
# Define probabilities for each outcome
outcome_probabilities = {
}