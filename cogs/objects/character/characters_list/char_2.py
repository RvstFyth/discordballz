'''
Manage the character 2

Last update: 26/06/19
'''

# Dependancies

import asyncio

# Object 

from cogs.objects.character.character import Character
    # Abilities
from cogs.objects.character.abilities.offensive.ability_acid import Ability_Acid
from cogs.objects.character.abilities.offensive.ability_acidExplosion import Ability_AcidExplosion
from cogs.objects.character.abilities.support.ability_replenishTheRanks import Ability_ReplenishTheRanks

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon, Get_type_icon
from cogs.utils.functions.commands.fight.functions.stat_manager import Set_stat

class Char_2(Character):
    '''
    Represents the Blue Saibaiman
    '''

    def __init__(self):
        Character.__init__(self)
        # Basic
        self.level = 150
        self.id = 2
        self.name = 'Blue Saibaiman'
        self.image = 'https://i.imgur.com/syjNBd2.png'
        self.thumb = 'https://i.imgur.com/wcKoXiB.png'
        self.icon = '<:saibaiman_b:589492373130706964>'
        self.saga = 0
        self.type_icon = 0
        self.type_value = 0
        self.rarity_icon = 0
        self.rarity_value = 5

        # Fight
        self.max_hp = 4250
        self.current_hp = 4250
        self.max_ki = 100
        self.current_ki = 0

        self.physical_damage_max = 250
        self.physical_damage_min = 225

        self.ki_damage_max = 400
        self.ki_damage_min = 360
        
        self.physical_defense = 700
        self.ki_defense = 625

        self.critical_chance = 10
        self.dodge_chance = 20
        
        self.ki_regen = 3

        self.dot = []
        self.buff = []
        self.debuff = []

        self.ability_list = [Ability_Acid, Ability_AcidExplosion, Ability_ReplenishTheRanks]

    # Methods

    async def init(self, client, ctx):
        '''
        `coroutine`

        Translation
        '''

        # Init

        _ = await Translate(client, ctx)

        self.name = _('Blue Saibaiman')

        self.rarity_icon = await Get_rarity_icon(self.rarity_value)
        self.type_icon = await Get_type_icon(self.type_value)

        await Set_stat(client, ctx, self)
        return
    
    async def Use_ability(self, client, ctx, caster, target, team_a, team_b, move: str, ability):
        '''
        `coroutine`
        '''

        # Init

        get_ability = self.ability_list[ability]
        ability_ = get_ability()
        
        await ability_.init(client, ctx, caster)

        return(ability_)