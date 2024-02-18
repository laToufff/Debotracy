from datetime import datetime

import discord as dc
from discord.ext import commands
from discord.commands import SlashCommandGroup

from ..database import get_guild, new_vote, get_votes_channel, get_vote_results_channel, add_vote_message
from ..database.models import Vote

from ..config import Bot
from ..utils import mention, Embed

class VoteCog (commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    vote_group = SlashCommandGroup(
        name='vote',
        description='Commands to create or interact with votes.'
    )
 
    @vote_group.command()
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
        embed.set_footer(text="Vote id: "+str(vote.id))
        channel = await get_votes_channel(ctx.guild)
        msg = await channel.send(embed=embed)
        await add_vote_message(vote.id, msg.id)
        await ctx.respond(f"Vote created in channel {mention.channel(channel)}.\nAdd options by running {mention.command('option add')}.", embed=embed, ephemeral=True)