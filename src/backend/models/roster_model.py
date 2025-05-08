from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional
from ..database.base import Base
from ..models import TeamModel, PlayerModel
    

class RosterModel(Base):
    """Database model for team rosters (both MLB and custom)."""
    __tablename__ = 'rosters'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    player_id: Mapped[int] = mapped_column(ForeignKey('players.id'))
    year: Mapped[Optional[int]] = mapped_column(nullable=True)  # Season year
    
    # Relationships
    team: Mapped[TeamModel] = relationship(back_populates="rosters")
    player: Mapped[PlayerModel] = relationship(back_populates="rosters") 