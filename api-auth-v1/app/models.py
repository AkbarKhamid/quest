from typing import Any, Dict

import humps

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String, func, inspect
from sqlalchemy.orm import relationship

from app.models.base import Base


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return humps.depascalize(cls.__name__)

    def dict(self) -> Dict[str, Any]:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    status = Column(Enum('new', 'not_new', 'banned', name='user_status'), default='new', nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', status='{self.status}')>"