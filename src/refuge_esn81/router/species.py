from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from refuge_esn81.database.database import get_db
from refuge_esn81.schemas.speciesSchema import Species, SpeciesCreate
from refuge_esn81.services.specieService import SpecieService


speciesRouter = APIRouter(prefix="/api/species", tags=["species"])


@speciesRouter.get("/", response_model=list[Species])
async def get_species(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    service = SpecieService()
    return service.get_species(db, skip=skip, limit=limit)


@speciesRouter.get("/{specie_id}", response_model=Species)
async def get_specie(specie_id: int, db: Session = Depends(get_db)):
    service = SpecieService()
    specie = service.get_specie(db, specie_id)
    if specie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Species not found")
    return specie


@speciesRouter.post("/", response_model=Species, status_code=status.HTTP_201_CREATED)
def create_new_species(specie: SpeciesCreate, db: Session = Depends(get_db)):
    service = SpecieService()
    try:
        return service.create_specie(db, specie)
    except ValueError as exc:  # pragma: no cover - defensive programming
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except IntegrityError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Species with this name already exists",
        ) from exc
