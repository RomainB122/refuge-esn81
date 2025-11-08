from fastapi import APIRouter, FastAPI, Depends, HTTPException
from refuge_esn81.models.animal import Animal
from refuge_esn81.schemas.animalSchema import AnimalCreate
from sqlalchemy.orm import Session
from refuge_esn81.database.database import get_db
from refuge_esn81.services.animalService import AnimalService


animalsRouter = APIRouter(prefix="/animals", tags=["animals"])

@animalsRouter.get("/animals")
async def get_animals():
    return 'animals'

@animalsRouter.post("/animals/", response_model=Animal)
def create_new_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    service = AnimalService()
    return service.create_animal(db, animal)