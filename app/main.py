import datetime

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import SessionLocal, engine
from app.schemas import Greeting


class LazyDbInit:
    """
    Create the db schema, just once.
    """
    is_initizalized = False

    @classmethod
    def initialize(cls):
        if not cls.is_initizalized:
            models.Base.metadata.create_all(bind=engine)
            cls.is_initizalized = True


server = FastAPI()


# Dependency
def get_db():
    # Create the db schema, if needed, before starting a session.
    # This is a workaround for an issue where the FastAPI server
    # may be started before the Postgresql db is ready.
    # I didn't manage to solve this in the docker-compose compose.yml file.
    # The healtcheck configuration doesn't seem to work.
    LazyDbInit.initialize()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@server.get("/", response_model=list[schemas.Greeting])
async def root(db: Session = Depends(get_db)):
    text = str(datetime.datetime.now())
    greeting = Greeting(text=text)
    db_greeting = models.Greeting(**greeting.dict())
    db.add(db_greeting)
    db.commit()
    return db.query(models.Greeting).all()

if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=8001)
