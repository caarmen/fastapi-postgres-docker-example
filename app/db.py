from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:azerty123@db/app")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
