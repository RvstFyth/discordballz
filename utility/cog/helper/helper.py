"""
Manages the helper.

--

Author : DrLarck

Last update : 29/08/19 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.graphic.embed import Custom_embed

# helper
class Helper:
    """
    Manages the help commands and other help messages.

    - Parameter :

    `client` : Represents a `discord.Client`.
    """
    
    def __init__(self, client, ctx):
        # base
        self.ctx = ctx
        self.client = client
        # embed
        self.embed = None

    # method
    async def help_command(self):
        return
    
    async def display_help(self, help_message):
        """
        `coroutine`

        Displays the help message.

        - Parameter :

        `help_message` : Represents an embedded message to send.
        """

        await self.ctx.send(embed = help_message)