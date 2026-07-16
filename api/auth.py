from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.auth import RegisterRequest
from app.schemas.auth import LoginRequest

from app.services.auth_service import AuthService

from app.auth.dependencies import get_current_user

router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    service = AuthService(db)

    try:
        user = service.register(request)

        return {
            "message": "User registered successfully",
            "id": user.id,
            "email": user.email
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    service = AuthService(db)

    request = LoginRequest(
        email=form_data.username,   # OAuth2 uses username field
        password=form_data.password
    )

    try:
        return service.login(request)

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

@router.get("/me")
def current_user(

    user=Depends(get_current_user)

):

    return user