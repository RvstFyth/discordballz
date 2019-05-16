'''
Manages the character's ability effects.

Last update: 14/05/19
'''

# Dependancies

import asyncio

async def Character_ability_effects(client, character, ability, fighter, opponent):
    '''
    `coroutine`

    Apply the effects of the ability to the correct object.

    `client` : must be `discord.Client` object.

    `character` : must be type `int` and represent the global id of the character.

    `ability` : must be type `int` and represent the player's choice.

    `fighter` : must be `Fighter` object.

    `opponent` : must be `Opponent` object.

    Return: `Fighter` object or `Opponent` object with the modified stats.
    '''

    if(character == 1):
        pass