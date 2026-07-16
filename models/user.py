from datetime import datetime
from enum import Enum

from sqlalchemy import Column, Integer, String, DateTime, Enum as SqlEnum

from app.database.database import Base


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    SUPPORT = "SUPPORT"
    CUSTOMER = "CUSTOMER"


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        SqlEnum(UserRole),
        default=UserRole.CUSTOMER,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )