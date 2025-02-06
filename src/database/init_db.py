from .base import Base, engine
from ..team import Team
from ..player import Player

def init_db():
    # Create all tables
    Base.metadata.create_all(engine) 