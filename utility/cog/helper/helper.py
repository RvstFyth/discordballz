"""
Manages the helper.

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
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
    
    # special
    async def summon(self):
        """
        `coroutine`

        Displays the command.help for the summon command.

        --

        Return : send a discord.Message (embedded)
        """

        # init
        self.embed = Custom_embed(self.client)
        summon_help = await self.embed.setup_embed()

        # setup
        # title and desc
        summon_help.add_field(
            name = "Summon commands :",
            value = "Welcome to the **Summon** help pannel.\n__Aliases__ : sum",
            inline = False
        )

        # commands
        summon_help.add_field(
            name = "d!summon",
            value = "Displays the command help.",
            inline = False
        )

        summon_help.add_field(
            name = "d!summon basic",
            value = "Summons a random character from the **Basic** expansion.",
            inline = False
        )

        return(summon_help)