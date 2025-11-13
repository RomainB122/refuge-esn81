from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from refuge_esn81.database.database import get_db
from refuge_esn81.schemas.animalSchema import Animal, AnimalCreate
from refuge_esn81.services.animalService import AnimalService
from refuge_esn81.services.specieService import SpecieService


animalsRouter = APIRouter(prefix="/api/animals", tags=["animals"])


@animalsRouter.get("/", response_model=list[Animal])
async def get_animals(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    service = AnimalService()
    return service.get_animals(db, skip=skip, limit=limit)


@animalsRouter.get("/{animal_id}", response_model=Animal)
async def get_animal(animal_id: int, db: Session = Depends(get_db)):
    service = AnimalService()
    animal = service.get_animal(db, animal_id)
    if animal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    return animal


@animalsRouter.post("/", response_model=Animal, status_code=status.HTTP_201_CREATED)
def create_new_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    species_service = SpecieService()
    if species_service.get_specie(db, animal.species_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Species not found",
        )

    service = AnimalService()
    return service.create_animal(db, animal)

