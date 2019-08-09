"""
Custom embed.

--

Authord : DrLarck

Last update : 15/07/19
"""

# dependancies
import asyncio
from discord.embeds import Embed

# config
from configuration.bot import bot_config

# class embed
class Custom_embed:
    """
    Defines the custom embed format for the messages.

    - Parameter :

    - Attribute :

    - Method :
    """

    # attribute
    def __init__(self, client, title = None, description = None, colour = None, footer = None, thumb = None):
        # bot
        self.client = client

        # embed
        self.title = title
        self.description = description
        self.colour = colour
        self.footer = footer
        self.thumb = thumb

        # run the setup
        self.client.loop.run_until_complete(self.setup_embed())

    # method
    async def setup_embed(self):
        """
        `coroutine`

        Setting up the embed format.

        --

        Return : `discord.Embed`
        """

        # init
        embed = Embed()
        embed.colour = 0xF54719

        # setting up
        if(self.title != None):
            embed.title = self.title
        
        if(self.description != None):
            embed.description = self.description
        
        if(self.colour != None):
            embed.colour = self.colour
        
        if(self.footer != None):
            embed.set_footer(text = self.footer, icon_url = self.client.user.avatar_url)
        
        else:
            embed.set_footer(text = f"v{bot_config['version']} - {bot_config['phase']} | Credit : DrLarck & DrMegas", icon_url = self.client.user.avatar_url)
        
        if(self.thumb != None):
            embed.set_thumbnail(url = self.thumb)

        embed.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
        
        return(embed)