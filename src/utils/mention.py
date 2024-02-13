from ..config import bot

def command(c: str) -> str:
    return f"</{c}:{bot.get_command(c).qualified_id}>"

def channel(id: int) -> str:
    return f"<#{id}>"