from src.database.database import *


#Function to connect with the session factory
#================================#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#================================#