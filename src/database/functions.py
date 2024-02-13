from .base import async_session
from .models import Guild


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