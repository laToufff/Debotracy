from datetime import datetime

import discord as dc
from discord.ext import commands
from discord.commands import SlashCommandGroup

from ..database import get_guild, new_vote
from ..database.models import Vote

from ..utils import mention, Embed

class VoteCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    vote_group = SlashCommandGroup(
        name='vote',
        description='Commands to create or interact with votes.'
    )

    @dc.option(
        name='title',
        description='The title of the vote.',
        type=str,
        required=True
    )
    @dc.option(
        name='description',
        description='The description of the vote.',
        type=str,
        required=True
    )
    @vote_group.command()
    async def create(self, ctx: dc.ApplicationContext, title: str, desc: str):
        """Initialize the creation of a vote."""
        vote = Vote(
            guild_id=ctx.guild.id,
            author_id=ctx.author.id,
            name=title,
            description=desc,
            multiple_choices=True,
            time_created=datetime.now(),
            is_open=True
        )
        vote = await new_vote(vote)
        embed = Embed(title=vote.name, description=vote.description, color=0x00aaff)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        await ctx.respond(f"Vote initialized with id {vote.id}.\nAdd options by running /option add.", embed=embed, ephemeral=True)