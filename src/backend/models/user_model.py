from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING
from ..database.base import Base

if TYPE_CHECKING:
    from ..models import TeamModel

class UserModel(Base):
    """Database model for user accounts.
    
    This model stores user account information and maintains relationships
    with their custom teams.
    
    Attributes:
        id: Unique identifier for the user
        username: Unique username for the user
        email: User's email address
        password_hash: Hashed version of the user's password
        teams: List of custom teams created by this user
    """
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    
    # Relationships
    teams: Mapped[list["TeamModel"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
    def to_dict(self) -> dict:
        """Convert model to dictionary, excluding sensitive information."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'custom_teams': [team.to_dict() for team in self.custom_teams]
        }