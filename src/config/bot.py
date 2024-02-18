import os
from dotenv import load_dotenv

import discord as dc

load_dotenv()

intents = dc.Intents.default()
bot = dc.Bot(intents=intents, debug_guilds=[int(os.getenv("DEBUG_GUILD"))])