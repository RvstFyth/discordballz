"""
Represents a command's help pannel.

--

Author : DrLarck

Last update : 08/01/2020 (DrLarck)
"""

# dependancies
import asyncio

# graphic
from utility.graphic.embed import Custom_embed

class Help_command:
    """
    Represents the command's help pannel.

    - Attribute :

    `name` (str) : The command's name

    `description` (str) : The command's description

    `invoke` (str) : The command that will invoke the command

    `aliases` (list) : The command's aliases

    `init_field` (dict[name, value, inline(bool)]) : The first field displayed in the custom embed

    `fields` (list) : Command's embed fields (list of dict[name, value, inline(bool)])

    - Method :

    :coro:`get_embed(client)` : Return the command's custom help panel
    """

    # attribute
    def __init__(self):
        self.name = ""
        self.description = ""
        self.invoke = ""
        self.aliases = []
        
        # custom embed
        self.fields = []
    
    # method
    async def get_embed(self, client):
        """
        `coroutine`

        Display the custom command's help pannel

        --

        Return : `discord.Embed`
        """

        # init
        self.init_field = {
            "name" : f"{self.name} command",
            "value" : f"Welcome to the **{self.name}** help pannel",
            "inline" : False
        }
        embed = await Custom_embed(client).setup_embed()
        aliases = ""

        if(len(self.aliases) > 0):
            self.init_field["value"] += "\n__Aliases__ : "

            for alias in self.aliases:
                aliases += f"`{alias}` "
            
            self.init_field["value"] += aliases

        # init field
        embed.add_field(
            name = self.init_field["name"],
            value = self.init_field["value"],
            inline = self.init_field["inline"]
        )

        # custom field
        for field in self.fields:
            embed.add_field(
                name = field["name"],
                value = field["value"],
                inline = False
            )

        return(embed)