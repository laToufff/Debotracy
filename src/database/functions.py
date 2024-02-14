from .base import async_session
from .models import Guild, Vote

from sqlalchemy.future import select


async def set_guild(guild_id: int, vote_channel: int, vote_result_channel: int) -> None:
    async with async_session() as session:
        guild = await session.get(Guild, guild_id)
        if guild:
            guild.votes_channel = vote_channel
            guild.vote_results_channel = vote_result_channel
        else:
            guild = Guild(id=guild_id, votes_channel=vote_channel, vote_results_channel=vote_result_channel)
            session.add(guild)
        await session.commit()

async def get_guild(guild_id: int) -> Guild:
    async with async_session() as session:
        return await session.get(Guild, guild_id)
    
async def new_vote(vote: Vote) -> Vote:
    async with async_session() as session:
        session.add(vote)
        await session.commit()
        return vote
    
async def get_vote(vote_id: int) -> Vote:
    async with async_session() as session:
        return await session.get(Vote, vote_id)
    
async def get_votes(guild_id: int, author_id: int = None) -> list[Vote]:
    async with async_session() as session:
        stmt = select(Vote).where(Vote.guild_id == guild_id)
        if author_id:
            stmt = stmt.where(Vote.author_id == author_id)
        stmt = stmt.order_by(Vote.time_created.desc())
        return (await session.execute(stmt)).scalars().all()