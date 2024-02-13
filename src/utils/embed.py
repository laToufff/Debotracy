from ..config import bot
from discord import Embed as dcEmbed

class Embed (dcEmbed):
    def __init__(self, title: str, color: int = 0x0000ff,*args, **kwargs):
        super().__init__(title=title, color=color, *args, **kwargs)
        self.set_footer(text=f"By {bot.user.name}", icon_url=bot.user.avatar)