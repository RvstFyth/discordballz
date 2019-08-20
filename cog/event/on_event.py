"""
Manages the built-in event.

--

Author : DrLarck

Last update : 20/08/19 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# config
from configuration.bot import Bot_config

# on event
class On_event(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        """
        `coroutine`

        Prints out a message when the client is ready. 

        Update the Bot class informations.

        --

        Return : None
        """

        # init
        message = f"""
{self.client.user.name} v{Bot_config.version} - {Bot_config.phase}

Connected to : {len(self.client.guilds)} guilds

Is now ready to use !

__________________________________________________________________________
        """

        # printing the message onto the terminal
        print(message)

        # set the bot to ready
        Bot_config.is_ready = True

def setup(client):
    client.add_cog(On_event(client))