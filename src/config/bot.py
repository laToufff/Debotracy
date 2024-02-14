import os
from dotenv import load_dotenv

import discord as dc

class Bot (dc.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.processed_votes = {}

    def init_vote(self, vote_id: int, msg: dc.Message) -> None:
        self.processed_votes[vote_id] = msg
    
    def get_creation_msg(self, vote_id: int) -> dc.Message:
        return self.processed_votes[vote_id]
    

load_dotenv()

intents = dc.Intents.default()
bot = Bot(intents=intents, debug_guilds=[int(os.getenv("DEBUG_GUILD"))])