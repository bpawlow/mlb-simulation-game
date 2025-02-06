from sqlalchemy.orm import sessionmaker
from .base import engine

Session = sessionmaker(bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
