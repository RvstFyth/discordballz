'''
Manages the displaying of the teams.

Last update: 28/05/19
'''

# Dependancies

import asyncio

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.readability.embed import Basic_embed

async def Pve_display_team(client, ctx, player, player_team, enemy_team):
    '''
    `coroutine`

    Displays the team of the player and of the enemy.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `player` : must be `discord.Member` object.

    `player_team` & `enemy_team` : must be list of `Fighter` objects.

    Return: discord.Message
    '''

    # Init

    _ = await Translate(client, ctx)

    display_player, display_enemy = '', ''

    # Player_team display

    for fighter in player_team:
        await asyncio.sleep(0)

        display_player += _('{} **{}** lv.{}\n').format(fighter.stat.rarity, fighter.stat.name, fighter.level)
    
    for enemy in enemy_team:
        await asyncio.sleep(0)

        display_enemy += _('{} **{}** lv.{}\n').format(enemy.stat.rarity, enemy.stat.name, enemy.level)
    
    # Set embed

    display = Basic_embed(client)
    display.add_field(name = _('{}\'s team :').format(player.name), value = display_player, inline = True)
    display.add_field(name = _('Enemy team :'), value = display_enemy, inline = True)

    await ctx.send(embed = display)