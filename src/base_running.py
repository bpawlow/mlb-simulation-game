"""
Logic for base running, including runner advancement and scoring.
"""

class BaseState:
    def __init__(self):
        self.bases = [False, False, False]  # First, Second, Third
        self.runs_scored = 0
    
    def advance_runners(self, hit_type, outs):
        # Implement runner advancement logic based on hit_type
        # Return number of runs scored
        pass