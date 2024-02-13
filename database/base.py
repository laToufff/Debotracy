import os
from dotenv import load_dotenv

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
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

AsyncSessionLocal: AsyncSession = sessionmaker(bind=engine, class_=AsyncSession)

async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)