from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository

from app.auth.password import hash_password, verify_password
from app.auth.jwt_handler import create_access_token


class AuthService:

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, request):

        if self.user_repository.exists_by_email(request.email):
            raise ValueError("Email already exists")

        user = User(
            username=request.username,
            email=request.email,
            password=hash_password(request.password)
        )

        return self.user_repository.create(user)

    def login(self, request):

        user = self.user_repository.find_by_email(request.email)

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(
            request.password,
            user.password
        ):
            raise ValueError("Invalid email or password")

        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    def get_user_by_email(self, email: str):
        return self.user_repository.find_by_email(email)