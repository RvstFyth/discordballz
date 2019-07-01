'''
Manages the Box.

Last update: 01/07/19
'''

# dependancies

import asyncio, discord
from discord.ext import commands
from discord.ext.commands import Cog

# utils
from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.commands.box.box_displayer import Display_box
from cogs.utils.functions.commands.box.box_reaction import Box_add_reaction
from cogs.utils.functions.commands.box.box_wait_for import Box_wait_for_reaction

class Cmd_Box(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def box(self, ctx, *, action: str = None):
        '''
        Display the player's box.
        '''

        # init
        _ = await Translate(self.client, ctx)

        player = ctx.message.author
        page = 1  # the page to display
        reactions = []  # the possible reactions the user can reply with

        # Normal display
        if(action == None):  # if the player didn't choose any action

            while page > 0:  # stop if page = 0
                await asyncio.sleep(0)

                box, total_page = await Display_box(self.client, ctx, page = page)

                # add icons to the box message
                reactions = await Box_add_reaction(box, page, total_page)   

                next_page = await Box_wait_for_reaction(self.client, box, player, reactions, page)

                # check if error
                if(next_page == 'False'):  # if there an error occured
                    await ctx.send(_('<@{}> An error occurred, closing the box.').format(player.id))
                    await box.delete()  # closing the box message
                    break  # stop everything
                
                else:  # if it's ok
                    if(next_page == 0):  # close
                        await box.delete()  # delete the box if the user wanted to 
                        break
                    
                    else:  # if the user didn't want to close
                        await box.delete()  # delete the message to replace it
                        page = next_page  # define the new page to display

            # end of while page > 0
        
        # Force the display of a page
        elif(action != None):
            action = action.split()

            if(len(action) == 2):  # if there is at least 2 values
                if(action[0].upper() == 'PAGE'):  # if the user wants to access a page
                    if(action[1].isdigit()):  # if the page is passed
                        page = int(action[1])

                        while page > 0:  # stop if page = 0
                            await asyncio.sleep(0)

                            box, total_page = await Display_box(self.client, ctx, page = page)

                            # add icons to the box message
                            reactions = await Box_add_reaction(box, page, total_page)   

                            next_page = await Box_wait_for_reaction(self.client, box, player, reactions, page)

                            # check if error
                            if(next_page == 'False'):  # if there an error occured
                                await ctx.send(_('<@{}> An error occurred, closing the box.').format(player.id))
                                await box.delete()  # closing the box message
                                break  # stop everything
                            
                            else:  # if it's ok
                                if(next_page == 0):  # close
                                    await box.delete()  # delete the box if the user wanted to 
                                    break
                                
                                else:  # if the user didn't want to close
                                    await box.delete()  # delete the message to replace it
                                    page = next_page  # define the new page to display
                    
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