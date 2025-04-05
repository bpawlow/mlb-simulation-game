from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..database.base import Base

class LineupModel(Base):
    __tablename__ = 'lineups'
    
    id = Column(Integer, primary_key=True)
    custom_team_id = Column(Integer, ForeignKey('custom_teams.id'))
    player_id = Column(String, ForeignKey('players.player_id'))
    batting_order = Column(Integer)  # 1-9 batting order position, N/A if not in lineup
    field_position = Column(String, nullable=False)  # Actual position they'll play
    
    # Relationships
    custom_team = relationship("CustomTeamModel", back_populates="lineup")
    player = relationship("PlayerModel") 
    