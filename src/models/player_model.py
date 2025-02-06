from sqlalchemy import Column, Integer, String, Float, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from ..database.base import Base

class PlayerModel(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    player_id = Column(String, unique=True)
    name = Column(String, nullable=False)
    positions = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))
    year = Column(Integer)
    age = Column(Integer)
    
    # Stats columns
    ab = Column(Integer)
    pa = Column(Integer)
    hits = Column(Integer)
    singles = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    home_runs = Column(Integer)
    strikeouts = Column(Integer)
    walks = Column(Integer)
    hbp = Column(Integer)
    fo = Column(Integer)
    go = Column(Integer)
    lo = Column(Integer)
    po = Column(Integer)
    
    team = relationship("TeamModel", back_populates="players") 