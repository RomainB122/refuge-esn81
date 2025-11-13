from sqlalchemy.orm import Session, joinedload

from refuge_esn81.schemas.animalSchema import AnimalCreate
from refuge_esn81.models.animal import Animal

class AnimalService:
    def create_animal(self, db: Session, animal: AnimalCreate):
        db_animal = Animal(
            name=animal.name,
            age=animal.age,
            description=animal.description,
            gender=animal.gender,
            photo_url=animal.photo_url,
            species_id=animal.species_id,
        )
        db.add(db_animal)
        db.commit()
        db.refresh(db_animal)

        return (
            db.query(Animal)
            .options(joinedload(Animal.species))
            .filter(Animal.id == db_animal.id)
            .first()
        )

    def get_animals(self, db: Session, skip: int = 0, limit: int = 100):
        return (
            db.query(Animal)
            .options(joinedload(Animal.species))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_animal(self, db: Session, animal_id: int):
        return (
            db.query(Animal)
            .options(joinedload(Animal.species))
            .filter(Animal.id == animal_id)
            .first()
        )
