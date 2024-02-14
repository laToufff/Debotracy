import discord as dc
from discord.ext import commands

class OptionCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    option_group = dc.SlashCommandGroup(
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
    @commands.slash_command()
    async def add(self, ctx: dc.ApplicationContext, emoji: str, desc: str, vote_id: int = -1):
        """Add an option to the vote."""
        pass