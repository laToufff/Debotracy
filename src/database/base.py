import os
from dotenv import load_dotenv

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.engine import URL

load_dotenv()

Base = declarative_base()

db_url = URL.create(
    drivername="postgresql+asyncpg",
    username="postgres",
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_CONTAINER_NAME'),
    port=5432,
    database="postgres"
)
engine = create_async_engine(db_url, echo=True)

async_session: AsyncSession = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)