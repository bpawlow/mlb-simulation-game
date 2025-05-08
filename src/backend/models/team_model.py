from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING, Optional
from ..database.base import Base

if TYPE_CHECKING:
    from ..models import UserModel, LineupModel, RosterModel

class TeamModel(Base):
    """Database model for user-created or existing teams."""
    __tablename__ = 'teams'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'))  # Null for MLB teams
    is_mlb_team: Mapped[bool] = mapped_column(default=True)
    
    # Relationships
    user: Mapped[Optional["UserModel"]] = relationship(back_populates="teams")
    rosters: Mapped[list["RosterModel"]] = relationship(back_populates="team", cascade="all, delete-orphan")
    lineup: Mapped[list["LineupModel"]] = relationship(back_populates="team", 
                                                     order_by="LineupModel.batting_order")
    
    def to_dict(self) -> dict:
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'user': self.user.to_dict() if self.user else None,
            'lineup': [player.to_dict() for player in self.lineup]
        }