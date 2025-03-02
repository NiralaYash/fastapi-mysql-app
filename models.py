from sqlalchemy import Table, Boolean, Column, Integer, String
from database import Base

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, index=True)
    artistname = Column(String(50), unique=True)

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    contributor = Column(String(100))
    artist_id = Column(Integer)