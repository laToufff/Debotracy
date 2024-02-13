from .base import AsyncSessionLocal
from .models import Guild


async def set_guild(guild_id: int, vote_channel: int, vote_result_channel: int) -> None:
    async with AsyncSessionLocal() as session:
        guild = Guild(id=guild_id, votes_channel=vote_channel, vote_results_channel=vote_result_channel)
        session.add(guild)
        await session.commit()

