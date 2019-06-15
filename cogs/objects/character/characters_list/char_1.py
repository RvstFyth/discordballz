'''
Manage the character_1

Last update: 15/06/19
'''

# Dependancies

import asyncio

# Objects

from cogs.objects.character.character import Character

# Abilities

from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid
from cogs.objects.character.abilities.offensive.ability_acid import Ability_Acid
from cogs.objects.character.abilities.offensive.ability_syphon import Ability_Syphon
from cogs.objects.character.abilities.support.ability_unityIsStrenght import Ability_UnityIsStrenght
from cogs.objects.character.abilities_effects.buff.unity_is_strenght import Unity_is_strenght

# Utils

from cogs.utils.functions.commands.fight.functions.stat_manager import Set_stat
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move
from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon, Get_type_icon
from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator

class Char_1(Character):
    '''
    Represents : `Green Saibaiman`

    The stats are based on the lv.1
    '''

    # Instance attributes

    def __init__(self):
        Character.__init__(self)
        # Basic
        self.level = 150
        self.id = 1
        self.name = 'Green Saibaiman'
        self.image = 'https://i.imgur.com/1m8rA7L.png'
        self.icon = '<:saibaiman_a:589485375685263373>'
        self.saga = 0
        self.type_icon = 0
        self.type_value = 0
        self.rarity_icon = 0
        self.rarity_value = 5

        # Fight
        self.max_hp = 3500
        self.current_hp = 3500
        self.max_ki = 100
        self.current_ki = 0

        self.physical_damage_max = 400
        self.physical_damage_min = 360  # The minimum damages represent 90 % of the max damages (90*max)/100 ou 0.9*max
        self.ki_damage_max = 850
        self.ki_damage_min = 765

        self.physical_defense = 475
        self.ki_defense = 400
        self.critical_chance = 10  # In %
        self.dodge_chance = 10  # In %
        self.ki_regen = 2
        self.health_regen = 0

        self.dot = []
        self.debuff = []
        self.buff = []

        # Abilities
        self.ability_list = [Ability_Acid, Ability_Syphon, Ability_UnityIsStrenght]  # Represents the number of abilities a character has

    # Method

    async def init(self, client, ctx):
        '''
        `coroutine`

        Mainly translates the character infos.

        Return: void
        '''

        # Translation

        _ = await Translate(client, ctx)

        # Name

        self.name = _('Green Saibaiman')

        # Icons

        self.rarity_icon = await Get_rarity_icon(self.rarity_value)
        self.type_icon = await Get_type_icon(self.type_value)

        # Set stats

        await Set_stat(client, ctx, self)
        return

    # Abilities

    async def Use_ability(self, client, ctx, caster, target, team_a, team_b, move: str, ability):
        '''
        `coroutine`
        '''

        # Init

        get_ability = self.ability_list[ability]
        ability_ = get_ability()
        
        await ability_.init(client, ctx, caster)

        return(ability_)