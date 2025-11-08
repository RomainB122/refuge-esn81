from pydantic import BaseModel
from refuge_esn81.schemas.speciesSchema import Species

class AnimalBase(BaseModel):
    name: str
    species_id: int

class AnimalCreate(AnimalBase):
    pass

class Animal(AnimalBase):
    id: int
    species: Species

    class Config:
        orm_mode = True
