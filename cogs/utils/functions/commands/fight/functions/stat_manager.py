'''
Manages the stat of a character.

Last update: 08/06/19
'''

# Dependancies

import asyncio

# Config

from configuration.main_config.unit_multiplier import LEVEL_MULTIPLIER

# Utils

from cogs.objects.character.characters_list.all_char import Get_char

async def Reset_stat(client, ctx, character):
    '''
    `coroutine`

    Reset the stats of a character object in function of its level, awakening and potential.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `character` : must be `Character` object.

    Return: `Character` object
    '''

    # Init

    reference = await Get_char(character.id)
    reference.level = character.level
    await reference.init(client, ctx)

    # Now edit the character

        # Basics
    character.max_hp = reference.max_hp
    character.max_ki = reference.max_ki

        # Damages
    character.physical_damage_max = reference.physical_damage_max
    character.physical_damage_min = reference.physical_damage_min
    character.ki_damage_max = reference.ki_damage_max
    character.ki_damage_min = reference.ki_damage_min

        # Defense
    character.physical_defense = reference.physical_defense
    character.ki_defense = reference.ki_defense
    character.damage_reduction = reference.damage_reduction

        # Special
    character.critical_chance = reference.critical_chance
    character.critical_bonus = reference.critical_bonus
    character.dodge_chance = reference.dodge_chance

        # Regen
    character.ki_regen = reference.ki_regen
    character.health_regen = reference.health_regen

        # Flag
    character.flag = reference.flag

    return(character)

async def Set_stat(client, ctx, character):
    '''
    `coroutine`

    Set the stat of a character in function of its level of upgrade.

    `client` : must be `discord.Client` object.

    `ctx` : must be `discord.ext.commands.Context` object.

    `character` : must be `Character` object.

    Return: `Character` object.
    '''

    # Init

    level = character.level
    health_multiplier = (1 + (character.rarity_value * 20) / 100) + (250 * character.training_item_health)
    physical_damage_multiplier = (1 + (character.rarity_value * 20) / 100 + (50 * character.training_item_physical_damage))
    physical_defense_multiplier = (1 + (character.rarity_value * 20) / 100 + (50 * character.training_item_physical_defense))
    ki_damage_multiplier = (1 + (character.rarity_value * 20) / 100 + (50 *character.training_item_ki_damage))
    ki_defense_multiplier = (1 + (character.rarity_value * 20) / 100 + (50 * character.training_item_ki_defense))
    # Level calculation for over_multiplier
    divided_level = level/100 
    if(divided_level < 1):
        divided_level = 1
    over_multiplier = (divided_level + ((character.star * 10) / 100))

    # Upgrade

        # Basics
    character.current_hp = int((character.current_hp*health_multiplier)*over_multiplier)
    character.max_hp = int((character.max_hp*health_multiplier)*over_multiplier)

        # Damages
    character.physical_damage_max = int((character.physical_damage_max*physical_damage_multiplier)*over_multiplier)
    character.physical_damage_min = int((character.physical_damage_min*physical_damage_multiplier)*over_multiplier)
    character.ki_damage_max = int((character.ki_damage_max*ki_damage_multiplier)*over_multiplier)
    character.ki_damage_min = int((character.ki_damage_min*ki_damage_multiplier)*over_multiplier)

        # Defense
    character.physical_defense = int((character.physical_defense*physical_defense_multiplier)*over_multiplier)
    character.ki_defense = int((character.ki_defense*ki_defense_multiplier)*over_multiplier)

    return(character)