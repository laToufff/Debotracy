import discord as dc
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = dc.Intents.default()
bot = dc.Bot(intents=intents, debug_guilds=[int(os.getenv("DEBUG_GUILD"))])

class Main (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot ready as {bot.user.name}!')

    @commands.slash_command()
    async def ping(self, ctx: dc.ApplicationContext):
        """This is just a test command."""
        await ctx.respond('Pong!', ephemeral=True)

bot.add_cog(Main(bot))

bot.run(os.getenv("TOKEN"))
