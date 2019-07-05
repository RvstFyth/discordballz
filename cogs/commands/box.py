'''
Manages the Box.

Last update: 05/07/19
'''

# dependancies

import asyncio, discord
from discord.ext import commands
from discord.ext.commands import Cog

# utils

from cogs.utils.functions.commands.box.regular_box.box_manager import Box_manager
from cogs.utils.functions.commands.box.id_box.box_id_manager import Box_id_manager

class Cmd_Box(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def box(self, ctx, *, action: str = None):
        '''
        Display the player's box.
        '''

        # init

        player = ctx.message.author
        page = 1  # the page to display

        # Normal display
        if(action == None):  # if the player didn't choose any action

            await Box_manager(self.client, ctx, player, page)
        
        # Force the display of a page
        elif(action != None):
            action = action.split()

            if(len(action) == 1):  # if only one elem is found in action
                if(action[0].isdigit()):  # if its a number
                    char_id = int(action[0])  # the id of the unique characters to display

                    await Box_id_manager(self.client, ctx, player, char_id, page)

            elif(len(action) == 2):  # if there is at least 2 values
                if(action[0].upper() == 'PAGE'):  # if the user wants to access a page
                    if(action[1].isdigit()):  # if the page is passed
                        page = int(action[1])

                        await Box_manager(self.client, ctx, player, page)
                    
                    else:  # if action[1] is not the page
                        return
                
                else:  # if action[0] isn't PAGE
                    return
            
            else:  # if the lenght is not 2
                return
        
        # End of the command
        return

def setup(client):
    client.add_cog(Cmd_Box(client))