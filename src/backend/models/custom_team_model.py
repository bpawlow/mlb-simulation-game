from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database.base import Base

class CustomTeamModel(Base):
    __tablename__ = 'custom_teams'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Relationships
    user = relationship("UserModel", back_populates="custom_teams")
    lineup = relationship("LineupModel", back_populates="custom_team") 