from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional
from ..database.base import Base
from .player_model import PlayerModel

class TeamModel(Base):
    __tablename__ = 'teams'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    players: Mapped[PlayerModel] = relationship(back_populates="team")