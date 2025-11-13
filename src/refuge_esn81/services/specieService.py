from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from refuge_esn81.schemas.speciesSchema import SpeciesCreate
from refuge_esn81.models.species import Species

class SpecieService:
    def create_specie(self, db: Session, specie: SpeciesCreate):
        name = specie.name.strip()
        if not name:
            raise ValueError("Species name cannot be empty")

        db_specie = Species(name=name)
        db.add(db_specie)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise
        db.refresh(db_specie)
        return db_specie

    def get_species(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Species).offset(skip).limit(limit).all()

    def get_specie(self, db: Session, specie_id: int):
        return db.query(Species).filter(Species.id == specie_id).first()
