from fastapi import APIRouter
router = APIRouter()

@router.get("/register")
async def register():
    return {"message": "User registration endpoint"}
