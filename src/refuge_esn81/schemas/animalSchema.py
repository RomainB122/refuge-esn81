from typing import Optional

from pydantic import BaseModel, Field

from refuge_esn81.schemas.speciesSchema import Species

class AnimalBase(BaseModel):
    name: str
    age: Optional[int] = Field(default=None, ge=0)
    description: Optional[str] = None
    gender: Optional[str] = None
    photo_url: Optional[str] = None
    species_id: int = Field(..., gt=0)

class AnimalCreate(AnimalBase):
    pass

class Animal(AnimalBase):
    id: int
    species: Species

    class Config:
        from_attributes = True
