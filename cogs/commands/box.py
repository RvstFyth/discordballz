'''
Manages the Box.

Last update: 04/07/19
'''

# dependancies

import asyncio, discord
from discord.ext import commands
from discord.ext.commands import Cog

# utils

from cogs.utils.functions.commands.box.box_updater import Box_update_page

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
        reactions = []  # the possible reactions the user can reply with

        # Normal display
        if(action == None):  # if the player didn't choose any action

            await Box_update_page(self.client, ctx, player, page)
        
        # Force the display of a page
        elif(action != None):
            action = action.split()

            if(len(action) == 2):  # if there is at least 2 values
                if(action[0].upper() == 'PAGE'):  # if the user wants to access a page
                    if(action[1].isdigit()):  # if the page is passed
                        page = int(action[1])

                        await Box_update_page(self.client, ctx, player, page)
                    
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