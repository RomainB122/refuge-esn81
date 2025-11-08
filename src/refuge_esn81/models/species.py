from sqlalchemy import Column, Integer, String
from refuge_esn81.database.database import Base

class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
