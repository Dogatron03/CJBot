from typing import Optional
from . import bot


@bot.command(name="mcp")
async def mappings(name: str, version: Optional[str] = None):
    pass