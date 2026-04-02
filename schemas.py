from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS POU PROFIL ---
class ProfilBase(BaseModel):
    biographie: str
    pays: str
    genre_musical: str

class ProfilCreate(ProfilBase):
    artiste_id: int

class Profil(ProfilBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS POU ARTISTE ---
class ArtisteBase(BaseModel):
    nom: str

class ArtisteCreate(ArtisteBase):
    pass

class Artiste(ArtisteBase):
    id: int
    profil: Optional[Profil] = None
    class Config:
        from_attributes = True

# --- SCHEMAS POU CHANSON ---
class ChansonBase(BaseModel):
    titre: str
    duree: str

class ChansonCreate(ChansonBase):
    album_id: int

class Chanson(ChansonBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS POU ALBUM ---
class AlbumBase(BaseModel):
    titre: str
    annee_sortie: int

class AlbumCreate(AlbumBase):
    artiste_id: int

class Album(AlbumBase):
    id: int
    chansons: List[Chanson] = []
    class Config:
        from_attributes = True

# --- SCHEMAS POU PLAYLIST ---
class PlaylistBase(BaseModel):
    nom: str

class PlaylistCreate(PlaylistBase):
    pass

class Playlist(PlaylistBase):
    id: int
    chansons: List[Chanson] = []
    class Config:
        from_attributes = True