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
    'hit': {
        HitType.SHORT_SINGLE: 0.45,
        HitType.MEDIUM_SINGLE: 0.25,
        HitType.LONG_SINGLE: 0.10,
        HitType.SHORT_DOUBLE: 0.08,
        HitType.LONG_DOUBLE: 0.05,
        HitType.TRIPLE: 0.02,
        HitType.HOME_RUN: 0.05,
        HitType.ERROR: 0.01,
        HitType.SACRIFICE: 0.01,
        HitType.WALK: 0.01,
        HitType.HBP: 0.01
    },
    'out': {
        OutType.STRIKE_OUT: 0.30,
        OutType.GROUND_OUT: 0.25,
        OutType.FLY_OUT: 0.20,
        OutType.GIDP: 0.05,
        OutType.LDIF: 0.10,
        OutType.SHORT_FLY: 0.05,
        OutType.MEDIUM_FLY: 0.03,
        OutType.LONG_FLY: 0.02
    }
}