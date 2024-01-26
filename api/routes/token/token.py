from fastapi import APIRouter

from routes.token.auth.verifyToken import get_tokenJWT

router = APIRouter()


@router.get("/token")
async def get_token():
    return {"token": get_tokenJWT()}