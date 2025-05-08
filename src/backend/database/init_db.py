from .base import Base, engine

def init_db():
    """Create all database tables."""
    # Create all tables
    Base.metadata.create_all(engine)