"""
Define a Team class that holds information about team members, lineup, etc
"""

class Team:
    def __init__(self, name, lineup):
        self.name = name
        self.lineup = lineup  # List of Player objects
