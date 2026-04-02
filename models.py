from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Tab pivot pou Many-to-Many ant Playlist ak Chanson
playlist_chanson = Table(
    "playlist_chanson",
    Base.metadata,
    Column("playlist_id", Integer, ForeignKey("playlists.id"), primary_key=True),
    Column("chanson_id", Integer, ForeignKey("chansons.id"), primary_key=True),
)

class Artiste(Base):
    __tablename__ = "artistes"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)

    profil = relationship("ProfilArtiste", back_populates="artiste", uselist=False)
    albums = relationship("Album", back_populates="artiste", cascade="all, delete-orphan")

class ProfilArtiste(Base):
    __tablename__ = "profils_artiste"
    id = Column(Integer, primary_key=True, index=True)
    biographie = Column(String)
    pays = Column(String)
    genre_musical = Column(String)
    artiste_id = Column(Integer, ForeignKey("artistes.id"), unique=True)

    artiste = relationship("Artiste", back_populates="profil")

class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    annee_sortie = Column(Integer)
    artiste_id = Column(Integer, ForeignKey("artistes.id"))

    artiste = relationship("Artiste", back_populates="albums")
    chansons = relationship("Chanson", back_populates="album", cascade="all, delete-orphan")

class Chanson(Base):
    __tablename__ = "chansons"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    duree = Column(String) # eg: "3:45"
    album_id = Column(Integer, ForeignKey("albums.id"))

    album = relationship("Album", back_populates="chansons")
    playlists = relationship("Playlist", secondary=playlist_chanson, back_populates="chansons")

class Playlist(Base):
    __tablename__ = "playlists"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)

    chansons = relationship("Chanson", secondary=playlist_chanson, back_populates="playlists")