'''
Manages the Char_3.

Last update : 17/06/19
'''

# dependancies

import asyncio

# object

from cogs.objects.character.character import Character

# abilities

from cogs.objects.character.abilities.offensive.ability_acid import Ability_Acid
from cogs.objects.character.abilities.offensive.ability_spreadingAcid import Ability_SpreadingAcid
from cogs.objects.character.abilities.support.ability_ParalyzingBurns import Ability_ParalyzingBurns

# utils

from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon, Get_type_icon
from cogs.utils.functions.commands.fight.functions.stat_manager import Set_stat

class Char_3(Character):

    def __init__(self):
        Character.__init__(self)
        # basic
        self.id = 3
        self.name = 'Red Saibaiman'
        self.image = 'https://i.imgur.com/mIIt7jL.png'
        self.icon = '<:saibaiman_c:589492379447197699>'
        self.saga = 0
        self.type_icon = 0
        self.type_value = 0
        self.rarity_icon = ''
        self.rarity_value = 5

        self.level = 150

        self.max_hp = 1625
        self.current_hp = 1625

        self.max_ki = 100
        self.current_ki = 0

        self.physical_damage_max = 475
        self.physical_damage_min = 427
        self.ki_damage_max = 550
        self.ki_damage_min = 495

        self.physical_defense = 625
        self.ki_defense = 475

        self.critical_chance = 20
        self.dodge_chance = 10

        self.ki_regen = 4

        self.buff = []
        self.debuff = []
        self.dot = []

        self.ability_list = [Ability_Acid, Ability_SpreadingAcid, Ability_ParalyzingBurns]
        self.passive_list = []
        self.leader_list = []

        self.while_attacked = []
        self.while_attacking = []

        self.dying = []
        self.while_dead = []

        self.can_resurrect = True

    async def init(self, client, ctx):
        '''
        `coroutine`

        Translate.
        '''

        _ = await Translate(client, ctx)

        self.name = _('Red Saibaiman')
        
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