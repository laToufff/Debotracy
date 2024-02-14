import discord as dc
import os

from dotenv import load_dotenv
from discord.ext import commands

from src import database as db
from src.cogs import Setup, Vote, Option
from src.config import bot

load_dotenv()

class Main (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot ready as {bot.user.name}!')
        await bot.change_presence(activity=dc.Game(name="with votes..."))
        await db.create_all()

    @commands.slash_command()
    async def ping(self, ctx: dc.ApplicationContext):
        """This is just a test command."""
        await ctx.respond('Pong!', ephemeral=True)

bot.add_cog(Main(bot))
bot.add_cog(Setup(bot))
bot.add_cog(Vote(bot))
bot.add_cog(Option(bot))

bot.run(os.getenv("TOKEN"))
