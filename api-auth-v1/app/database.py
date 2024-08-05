from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_async_engine(settings.POSTGRES_URI)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)