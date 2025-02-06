from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database.base import Base

class TeamModel(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    players = relationship("PlayerModel", back_populates="team") 