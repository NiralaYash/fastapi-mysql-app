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

db_dependency = Annotated[Session,Depends(get_db)]


## Song CRUD Operations
@app.post("/songs/", status_code=status.HTTP_201_CREATED)
async def create_song(song: SongBase, db: db_dependency):
    db_song = models.Song(**song.model_dump())
    db.add(db_song)
    db.commit()

@app.get("/songs/{song_Id}", status_code= status.HTTP_200_OK)
async def read_song(song_Id: int, db: db_dependency):
    song = db.query(models.Song).filter(models.Song.id == song_Id).first()
    if song is None:
        HTTPException(status_code=404, detail='Song was not found')
    return song

# TODO Song Update

@app.delete("/songs/{song_Id}", status_code= status.HTTP_200_OK)
async def delete_song(song_Id: int, db: db_dependency):
    db_song = db.query(models.Song).filter(models.Song.id == song_Id).first()
    if db_song is None:
        raise HTTPException(status_code=404, detail='Song was not found')
    db.delete(db_song)
    db.commit()


## Artist CRUD Operations
@app.post("/artists/", status_code=status.HTTP_201_CREATED)
async def create_artist(artist: ArtistBase, db: db_dependency):
    db_artist = models.Artist(**artist.model_dump())
    db.add(artist)
    db.commit()

@app.get("/artists/{artist_Id}", status_code= status.HTTP_200_OK)
async def read_artist(artist_Id: int, db: db_dependency):
    artist = db.query(models.Artist).filter(models.Artist.id == artist_Id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail='Artist was not found')
    return artist

# TODO Artist Update

@app.delete("/artists/{artist_Id}", status_code= status.HTTP_200_OK)
async def delete_artist(artist_Id: int, db: db_dependency):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_Id).first()
    if db_artist is None:
        raise HTTPException(status_code=404, detail='Artist was not found')
    db.delete(db_artist)
    db.commit()