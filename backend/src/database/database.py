from .imports import *


SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_recycle=3600,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()