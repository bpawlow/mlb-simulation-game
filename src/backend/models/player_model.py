from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional
from ..database.base import Base
from .team_model import TeamModel

class PlayerModel(Base):
    """Database model for player records."""
    __tablename__ = 'players'
    
    # Use modern SQLAlchemy 2.0 style annotations
    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    positions: Mapped[str] = mapped_column(String(200))
    team_id: Mapped[Optional[int]] = mapped_column(ForeignKey('teams.id'))
    year: Mapped[int]
    age: Mapped[int]
    
    # Stats columns with explicit types
    ab: Mapped[int] = mapped_column(default=0)
    pa: Mapped[int] = mapped_column(default=0)
    hits: Mapped[int] = mapped_column(default=0)
    singles: Mapped[int] = mapped_column(default=0)
    doubles: Mapped[int] = mapped_column(default=0)
    triples: Mapped[int] = mapped_column(default=0)
    home_runs: Mapped[int] = mapped_column(default=0)
    strikeouts: Mapped[int] = mapped_column(default=0)
    walks: Mapped[int] = mapped_column(default=0)
    hbp: Mapped[int] = mapped_column(default=0)
    fo: Mapped[int] = mapped_column(default=0)
    go: Mapped[int] = mapped_column(default=0)
    lo: Mapped[int] = mapped_column(default=0)
    po: Mapped[int] = mapped_column(default=0)
    
    # Relationships
    team: Mapped[TeamModel] = relationship(back_populates="players")
    
    # Add methods for serialization
    def to_dict(self) -> dict:
        """Convert model to dictionary."""
        return {
            'player_id': self.player_id,
            'name': self.name,
            'positions': self.positions,
            'team_id': self.team_id,
            'year': self.year,
            'age': self.age,
            'stats': {
                'ab': self.ab,
                'pa': self.pa,
                'hits': self.hits,
                'singles': self.singles,
                'doubles': self.doubles,
                'triples': self.triples,
                'home_runs': self.home_runs,
                'strikeouts': self.strikeouts,
                'walks': self.walks,
                'hbp': self.hbp,
                'fo': self.fo,
                'go': self.go,
                'lo': self.lo,
                'po': self.po
            }
        } 