import binascii
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from routes.token.auth.config import SECRET_KEY, ALGORITHM
from jose import JWTError, jwt


def get_tokenJWT() -> str:
    return SECRET_KEY


def verify_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl=SECRET_KEY))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )



