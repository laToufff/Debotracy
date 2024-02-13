import discord as dc
from discord.ext import commands

from ..database import set_guild, get_guild
from ..utils import mention, Embed

class Setup (commands.Cog):
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

    @commands.slash_command()
    async def info(self, ctx: dc.ApplicationContext):
        """Get the current setup of the guild."""
        guild = await get_guild(ctx.guild.id)
        embed = Embed(title=f'Current setup for {ctx.guild.name} :', color=0x0000ff)
        if guild:
            embed.description = f"These values can be changed at any time using the {mention.command('setup')} command"
            embed.add_field(name='Votes channel :', value=mention.channel(guild.votes_channel), inline=True)
            embed.add_field(name='Vote results channel :', value=mention.channel(guild.vote_results_channel), inline=True)
        else:
            embed.description = f"This guild has not been setup yet. Please setup the guild with {mention.command('setup')}."
        await ctx.respond(embed=embed, ephemeral=True)
        
        