from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..database.base import Base
from ..models import TeamModel, PlayerModel

class LineupModel(Base):
    """Database model for custom team lineups."""
    __tablename__ = 'lineups'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    player_id: Mapped[str] = mapped_column(ForeignKey('players.id'))
    batting_order: Mapped[int] = mapped_column(nullable=False)  # 1-9 batting order position
    field_position: Mapped[str] = mapped_column(String(10), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)  # For managing multiple lineups
    
    # Relationships
    team: Mapped[TeamModel] = relationship(back_populates="lineup")
    player: Mapped[PlayerModel] = relationship(back_populates="lineup_spots")
    
    def to_dict(self) -> dict:
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'custom_team_id': self.custom_team_id,
            'player_id': self.player_id,
            'batting_order': self.batting_order,
            'field_position': self.field_position,
            'team': self.team.to_dict(),
            'player': self.player.to_dict() if self.player else None
        }