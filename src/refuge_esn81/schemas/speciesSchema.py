from pydantic import BaseModel, Field

class SpeciesBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)

class SpeciesCreate(SpeciesBase):
    pass

class Species(SpeciesBase):
    id: int

    class Config:
        from_attributes = True

