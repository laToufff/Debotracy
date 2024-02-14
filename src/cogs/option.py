import discord as dc
from discord.ext import commands
from discord.commands import SlashCommandGroup

from ..database import get_votes
from ..utils import mention
from ..config import Bot

class OptionCog (commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    option_group = SlashCommandGroup(
        name='option',
        description='Commands to create or interact with options.'
    )

    @dc.option(
        name='emoji',
        description='The emoji used for the reactions.',
        type=str,
        required=True
    )
    @dc.option(
        name='description',
        description='The description of the option.',
        type=str,
        required=True
    )
    @dc.option(
        name='vote id',
        description='The id of the vote to add the option to. Defaults to the last vote you created.',
        type=int,
        required=False
    )
    @option_group.command()
    async def add(self, ctx: dc.ApplicationContext, emoji: str, desc: str, vote_id: int = -1):
        """Add an option to the vote."""
        votes = await get_votes(ctx.guild.id, ctx.author.id)
        if not votes:
            await ctx.respond(f"You have not created any votes on this server yet. Please start the vote creating process with {mention.command('vote create')}", ephemeral=True)
            return
        if vote_id == -1:
            vote_id = votes[0].id
        if vote_id not in [vote.id for vote in votes]:
            await ctx.respond(f"You have not created a vote with the id {vote_id} on this server.", ephemeral=True)
            return
        msg = self.bot.get_creation_msg(vote_id)
        #chnl = await ctx.guild.fetch_channel(msg.channel.id)
        #msg = await chnl.fetch_message(msg.id)
        await msg.add_reaction(emoji)
        embed = msg.embeds[0]
        embed.add_field(name=emoji, value=desc, inline=True)
        await msg.edit(embed=embed)
        await ctx.respond(f"Option added to vote with id {vote_id}.", ephemeral=True)