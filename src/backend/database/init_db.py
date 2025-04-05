from .base import Base, engine
from ..classes.team import Team
from ..classes.player import Player

def init_db():
    # Create all tables
    Base.metadata.create_all(engine) 