from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

Base = declarative_base()

engine = create_async_engine('sqlite+aiosqlite:///data/database.db', echo=True)

AsyncSessionLocal: AsyncSession = sessionmaker(bind=engine, class_=AsyncSession)

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)