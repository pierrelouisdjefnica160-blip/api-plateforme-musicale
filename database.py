from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Defini non fichye baz de done a (li pral kreye otomatikman nan katab la)
SQLALCHEMY_DATABASE_URL = "sqlite:///./music_platform.db"

# 2. Kreye "engine" lan
# Nou mete check_same_thread=False paske SQLite mande sa pou l ka travay byen ak FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Kreye yon sesyon pou nou ka fè operasyon yo (Ajoute, Li, Modifye, Supprime)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Kreye klas "Base" la. Tout modèl nou yo (Artiste, Album, etc.) pral eritye de li
Base = declarative_base()

# Fonksyon pou nou ka jwenn yon sesyon baz de done nan route yo
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        