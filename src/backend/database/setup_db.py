from .init_db import init_db
from .session import Session
from ..models.team_model import TeamModel
from ..models.player_model import PlayerModel
from ..models.user_model import UserModel
from ..database.base import Base, engine
import pandas as pd

def setup_database():
    
    # Drop all existing tables
    Base.metadata.drop_all(bind=engine)
    
    # Initialize database schema
    init_db()
    
    # Create database session
    db = Session()
    
    try:        
        # Create default admin user if it doesn't exist
        admin_user = db.query(UserModel).filter_by(username="admin_user").first()
        if not admin_user:
            admin_user = UserModel(
                username="admin",
                email="bradleypawlow99@gmail.com",
                password_hash="admin1"
            )
            db.add(admin_user)
            db.commit()
        
        
        # Load existing players CSV data
        players_df = pd.read_csv('data/players.csv')
        
        # Group players by team
        for team_name, team_players in players_df.groupby('team'):
            # Create team
            team = TeamModel(name=team_name)
            db.add(team)
            db.flush()  # This gets us the team.id
            
            # Create players for this team
            for _, player_data in team_players.iterrows():
                player = PlayerModel(
                    player_id=player_data['player_id'],
                    name=player_data['name'],
                    positions=player_data['position'],
                    year=player_data['year'],
                    age=player_data['player_age'],
                    # Stats
                    ab=player_data['ab'],
                    pa=player_data['pa'],
                    hits=player_data['hit'],
                    singles=player_data['single'],
                    doubles=player_data['double'],
                    triples=player_data['triple'],
                    home_runs=player_data['home_run'],
                    strikeouts=player_data['strikeout'],
                    walks=player_data['walk'],
                    hbp=player_data['b_hit_by_pitch'],
                    fo=player_data['b_out_fly'],
                    go=player_data['b_out_ground'],
                    lo=player_data['b_out_line_drive'],
                    po=player_data['b_out_popup']
                )
                db.add(player)
        
        db.commit()
        print("Database initialized and populated successfully!")
        
    except Exception as e:
        print(f"Error setting up database: {e}")
        db.rollback()
    finally:
        db.close()