'''
Manages the fight system.

Last update: 15/05/19
'''

# Dependancies

import asyncio

# Database

from cogs.utils.functions.database.select.player.player import Select_player_fighter

# Utils

from cogs.utils.functions.readability.embed import Basic_embed
from cogs.utils.functions.commands.fight.displayer.player_displayer import Display_player_fighter

# Objects

from cogs.objects.character import Character
from cogs.objects.fighter import Fighter

async def Fight(client, ctx, player):    
    '''
    This must be designed to be used with every game mode.
    '''
    
    # Init

    player_fighter = await Select_player_fighter(client, player)

    if(player_fighter['unique id'] != 'None'):
        # If the player has set a fighter

        character_ = Character(client, player_fighter['global id'])  # Store the character's informations at the passed global id
        
        fighter_ = Fighter(client, player_fighter['unique id'], character_)
        fighter_.BASE_HP = await fighter_.base_hp()
        
        # We start the fight
            # Init
        
        turn = 1

        while(fighter_.current_hp > 0):
            
            await Display_player_fighter(client, ctx, player)
            fighter_.current_hp = 0
            turn += 1