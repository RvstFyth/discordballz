"""
Manages the hourly command

Last update: 12/07/19
"""

# dependancies

import asyncio
from discord.ext import commands
from time import time, strftime, gmtime

# utils

from cogs.objects.player.player import Player
from cogs.utils.functions.commands.hourly.hourly import Hourly

# graphics

from configuration.graphic_config.icons_config import ICON_DS, ICON_ZENIS

class Cmd_Hourly(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases = ["hr"])
    async def hourly(self, ctx):
        """
        The player gainsbonuses by doing hourly commands.
        """ 

        # init
        hourly_reward = {
            'stone' : 5,
            'zenis' : 50,
            "player xp" : 0
        }

        caller = ctx.message.author
        player = Player(self.client, caller)
        await player.init()

        _hourly = Hourly(self.client, player)
        now = time()

        # get player hourly infos
        # min and max represent the time limite to use the command
        hourly_info = {
            'min' : 3600,
            'max' : 7200,
            'hourly' : await _hourly.get_hourly(),
            'combo' : await _hourly.get_combo()
        }

        elapsed_time = now - hourly_info['hourly']  # get the elapsed time from the last hourly

        # now check if the player can hourly or not

        if(elapsed_time >= hourly_info['min']):  # if more than an hour has passed
            combo = hourly_info['combo']

            if(elapsed_time < hourly_info['max']):  # if the player re use the hourly before the limite is passed
                combo += 1
                await _hourly.update_combo(combo)
            
            else:  # reset the combo if the max time has passed
                combo = 0
                await _hourly.update_combo(combo)
            
            # give resources to the player
            combo_bonus = pow(1.10, 1+combo)

            stone_reward = int(hourly_reward['stone']*combo_bonus)
            zenis_reward = int(hourly_reward['zenis']*combo_bonus)

            await player.add_dragonstones(stone_reward)
            await player.add_zenis(hourly_reward['zenis']*combo_bonus)

            await ctx.send(f"<@{player.id}> You've received **{stone_reward:,}**{ICON_DS} as well as **{zenis_reward:,}**{ICON_ZENIS} !\nCombo : x{combo:,}")
            
            # reset the timer
            await _hourly.update_hourly(now)
        
        else:  # if the elapsed time is not enough, display the remaining time as a timer
            time_remaining = await _hourly.time_remaining()

            await ctx.send(f"<@{player.id}> It's too early for your `hourly`, come back in {time_remaining} !")
            
            return

def setup(client):
    client.add_cog(Cmd_Hourly(client))