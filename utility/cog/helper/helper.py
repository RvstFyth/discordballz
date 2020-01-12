"""
Manages the helper.

--

Author : DrLarck

Last update : 12/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# utils
from utility.graphic.embed import Custom_embed
from utility.cog.player.attribute.box.box import Box

# help command
from utility.cog.helper.command._summon import Help_summon
from utility.cog.helper.command._box import Help_box
from utility.cog.helper.command._fighter import Help_fighter
from utility.cog.helper.command._profile import Help_profile
from utility.cog.helper.command._show import Help_show
from utility.cog.helper.command._start import Help_start

# helper
class Helper:
    """
    Manages the help commands and other help messages.

    - Parameter :

    `client` : Represents a `discord.Client`.

    `ctx` : `discord.ext.commands.context`

    - Attribute : 

    `ctx`

    `client`

    `embed`

    `commands` : The help commands to display

    - Method : 

    :coro:`helper_manager()` : Manage the help command display

    :coro:`help_command(current_page)` : Display the help pannel

    :coro:`get_help_command(command_name)` : Get the help pannel for the command that is passed

    :coro:`display_help(help_message)` : Display the help pannel of a command
    """
    
    def __init__(self, client, ctx, player):
        # base
        self.ctx = ctx
        self.client = client
        # embed
        self.embed = None

        self.commands = [
            Help_start(),
            Help_box(), Help_fighter(), Help_profile(),
            Help_show(), Help_summon() 
        ]

        # util
        self.player = player
        self.box = Box(self.ctx, self.client, self.player)  # util for the reactions

    # method
    async def helper_manager(self):
        """
        Manage the helper displaying

        --

        Return : `None`
        """

        # init
        display, current_page, total_page = None, 1, 1

        # set
        total_page = int(((len(self.commands) - 1) // 5) + 1)

        while current_page > 0:
            await asyncio.sleep(0)

            # display the help
            help_pannel = await self.help_command(current_page, total_page)

            reaction_added = await self.box.add_button(help_pannel, current_page, total_page)

            reaction_ = await self.box.wait_for_reaction(help_pannel, self.player, reaction_added)

            await help_pannel.delete()

            if(reaction_ == None):
                break
            
            if(reaction_ == "❌"):
                current_page = 0        
            
            if(reaction_ == "⏮"):
                current_page = 1
            
            if(reaction_ == "⏭"):
                current_page = total_page
            
            if(reaction_ == "▶"):
                current_page += 1
            
            if(reaction_ == "◀"):
                current_page -= 1

        return

    async def help_command(self, current_page, total_page):
        """
        `coroutine`

        Display the help pannel.

        --

        Return : `discord.Message`
        """

        # init
        help_embed = await Custom_embed(self.client, title = "Help panel", description = f"Prefixes : `d!`, `db` | Support server : [Click here](https://discord.gg/eZf2p7h) \nPage {current_page} / {total_page}").setup_embed()
        start_at, end_at = 0 + 5 * (current_page - 1), 5 * current_page

        if(len(self.commands) < 5):
            end_at = len(self.commands)

        for a in range(start_at, end_at):
            if(a == len(self.commands)):
                break

            command = self.commands[a]

            help_embed.add_field(
                name = command.invoke,
                value = f"{command.description} | use `d!help {command.invoke}` for more infos.",
                inline = False
            )
        
        help_pannel = await self.ctx.send(embed = help_embed)

        return(help_pannel)
    
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