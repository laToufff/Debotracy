from ..config import bot
from discord import Embed as dcEmbed

class Embed (dcEmbed):
    def __init__(self, title: str, color: int = 0x0000ff,*args, **kwargs):
        super().__init__(title=title, color=color, *args, **kwargs)
        self.default_footer()

    def set_footer(self, text: str):
        super().set_footer(text=bot.user.name+" | "+text, icon_url=self.footer.icon_url)

    def default_footer(self):
        super().set_footer(text=bot.user.name, icon_url=bot.user.avatar)