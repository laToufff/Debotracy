import discord as dc
from discord.ext import commands

from database import set_guild

class Config (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dc.option(name='votes channel', 
                     description='Where the votes will be posted.', 
                     type=dc.TextChannel, 
                     required=True)
    @dc.option(name='vote results channel',
                     description='Where the vote results will be posted.',
                     type=dc.TextChannel,
                     required=True)
    @commands.slash_command()
    async def setup(self, ctx: dc.ApplicationContext, vote_channel: dc.TextChannel, vote_result_channel: dc.TextChannel):
        """Setup the channels needed for the bot to work."""
        await set_guild(ctx.guild.id, vote_channel.id, vote_result_channel.id)
        await ctx.respond('Guild setup successfully!', ephemeral=True)