"""
Manages the helper.

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.graphic.embed import Custom_embed

# help command
from utility.cog.helper.command._summon import Help_summon

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

        self.commands = [
            Help_summon()
        ]

    # method
    async def help_command(self):
        """
        `coroutine`

        Display the help pannel.

        --

        Return : `None`
        """

        # init
        help_embed = await Custom_embed(self.client, title = "Help pannel", description = "Prefixes : `d!`, `db`").setup_embed()

        for command in self.commands:
            help_embed.add_field(
                name = command.invoke,
                value = f"{command.description} | use `d!help {command.invoke}` for more infos."
            )
        
        await self.ctx.send(embed = help_embed)
    
    async def get_help_command(self, command_name):
        """
        `coroutine`

        Get the command help pannel

        --

        Return : `discord.Embed` or `None` if not found
        """

        # init
        help_pannel = None

        for command in self.commands:
            if(command_name.lower() == command.invoke or command_name.lower() == command.name.lower()):
                help_pannel = await command.get_embed(self.client)
        
        return(help_pannel)

    async def display_help(self, help_message):
        """
        `coroutine`

        Displays the help message.

        - Parameter :

        `help_message` : Represents an embedded message to send.
        """

        await self.ctx.send(embed = help_message)