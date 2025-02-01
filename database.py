from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
DATABASE_URL = "postgresql://postgres:postgres.fastapi@localhost:5432/Event"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 #Dependency to get the database session
def get_db():
    db = SessionLocal()  # Open a session
    try:
        yield db  # Yield the session to be used in the route
    finally:
        db.close()  # Close the session after the request is done

