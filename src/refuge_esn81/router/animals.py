from fastapi import APIRouter, FastAPI, Depends, HTTPException
from refuge_esn81.schemas.animalSchema import Animal, AnimalCreate
from sqlalchemy.orm import Session
from refuge_esn81.database.database import get_db
from refuge_esn81.services.animalService import AnimalService

animalsRouter = APIRouter(prefix="/animals", tags=["animals"])

@animalsRouter.get("/", response_model=list[Animal])
async def get_species(db: Session = Depends(get_db)):
    service = AnimalService()
    return service.get_animals(db)

@animalsRouter.post("/", response_model=Animal)
def create_new_species(animal: AnimalCreate, db: Session = Depends(get_db)):
    service = AnimalService()
    return service.create_animal(db, animal)