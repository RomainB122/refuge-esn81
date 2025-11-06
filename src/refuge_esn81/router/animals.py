from fastapi import APIRouter


animalsRouter = APIRouter(prefix="/animals", tags=["animals"])

@animalsRouter.get("/animals")
async def get_animals():
    return 'animals'

