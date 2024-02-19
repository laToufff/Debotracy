import discord as dc

from .base import async_session
from .models import Guild, VoteMessage

from sqlalchemy.future import select


async def get(cls: type, id: int = None, **kwargs):
    """Get an object of type `cls` from the database by its id if provided, or otherwise by its attributes.
    >>> guild: Guild = await get(Guild, ctx.guild.id)"""

    async with async_session() as session:
        if id:
            return await session.get(cls, id)
        return (await session.execute(select(cls).filter_by(**kwargs))).scalars().first()
    
async def get_all(cls: type, order_by = None, **kwargs) -> list:
    """Get all objects of type `cls` from the database that match the provided attributes. If `order_by` is provided, the results will be sorted accordingly.
    >>> votes: list[Vote] = await get_all(Vote, guild_id=ctx.guild.id, is_open=True, ...)"""

    async with async_session() as session:
        stmt = select(cls).filter_by(**kwargs)
        stmt = stmt.order_by(order_by)
        return (await session.execute(stmt)).scalars().all()
    
async def edit(cls: type, id: int, **kwargs):
    """Edit the object of type `cls` with the provided `id`, changing the attributes to the provided values.
    >>> await edit(Guild, ctx.guild.id, votes_channel=...)"""

    async with async_session() as session:
        obj = await session.get(cls, id)
        for k, v in kwargs.items():
            setattr(obj, k, v)
        await session.commit()
        return obj
    
async def new(cls: type, **kwargs):
    """Create a new object of type `cls` with the provided attributes.
    >>> vote: Vote = await new(Vote, guild_id=ctx.guild.id, ...)"""

    async with async_session() as session:
        obj = cls(**kwargs)
        session.add(obj)
        await session.commit()
        return obj
    
async def add(obj: object):
    """Add the provided object to the database.
    >>> await add(vote)"""

    async with async_session() as session:
        session.add(obj)
        await session.commit()
        return obj
    
async def set(cls: type, id: int, **kwargs):
    """Set the object of type `cls` with the provided `id`, changing the attributes to the provided values if it exists, or creating a new object with the provided attributes if it doesn't.
    >>> await set(Guild, ctx.guild.id, votes_channel=...)"""

    async with async_session() as session:
        if obj := await session.get(cls, id):
            for k, v in kwargs.items():
                setattr(obj, k, v)
        else:
            obj = cls(id=id, **kwargs)
            session.add(obj)
        await session.commit()
        return obj
    
async def get_channel(guild: dc.Guild, name: str) -> dc.TextChannel:
    id: int = getattr(await get(Guild, guild.id), name, None)
    return await guild.fetch_channel(id)
    
async def get_votes_channel(guild: dc.Guild) -> dc.TextChannel:
    return await get_channel(guild, 'votes_channel')

async def get_vote_results_channel(guild: dc.Guild) -> dc.TextChannel:
    return await get_channel(guild, 'vote_results_channel')

async def get_vote_message(vote_id: int, guild: dc.Guild) -> dc.Message:
    id: int = (await get(VoteMessage, vote_id=vote_id)).id
    return await (await get_votes_channel(guild)).fetch_message(id)