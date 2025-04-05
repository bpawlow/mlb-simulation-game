from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database.base import Base

class UserModel(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    
    # Relationships
    custom_teams = relationship("CustomTeamModel", back_populates="user") 