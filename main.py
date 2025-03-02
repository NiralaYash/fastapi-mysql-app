from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, Sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()

class SongBase(BaseModel):
    title: str
    contributor: str
    artist_id: int

class ArtistBase(BaseModel):
    artistname: str

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session,Depends(get_db)]

@app.post("/songs", status_code=status.HTTP_201_CREATED)
async def create_song(song: SongBase, db: db_dependancy):
    db_song = models.Song(**song.model_dump())