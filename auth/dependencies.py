from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.auth.jwt_handler import decode_access_token

from app.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/auth/login"

)


def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    payload = decode_access_token(token)

    if payload is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid token"

        )

    email = payload.get("sub")

    service = AuthService(db)

    user = service.get_user_by_email(email)

    if user is None:

        raise HTTPException(

            status_code=401,

            detail="User not found"

        )

    return user