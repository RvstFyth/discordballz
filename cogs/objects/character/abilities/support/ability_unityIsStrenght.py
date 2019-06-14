'''
Manages the Unity is strenght ability

Last update: 14/06/19
'''

# Dependancies

import asyncio

# utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move

    # Effects
from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_buff
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_buff

# Object

from cogs.objects.character.abilities.ability import Ability
from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid
from cogs.objects.character.abilities_effects.buff.unity_is_strenght import Unity_is_strenght

class Ability_UnityIsStrenght(Ability):

    icon = '<:unity_is_strenght:585503883133059074>'
    id = 3

    def __init__(self):
        Ability.__init__(self)
        # Basic
        self.name = 'Unity is strenght'
        self.description = ''

        # Conifg
        self.can_target_ally = True
        self.need_target = False
        self.cost = 60
        self.cooldown = 0

    # Method

    async def init(self, client, ctx, caster):
        '''
        `coroutine`

        Translation

        `client` : must be `discord.Client` object.

        `ctx` : must be `discord.ext.commands.Context` object.

        `caster` : must be `Character` object of the character who uses the ability.

        Return: void
        '''

        # Init

        _ = await Translate(client, ctx)

        # Translate

        self.name = _('Unity is strenght')
        self.description = _('Damages dealt with {} this turn heal this character for **10 %** of his Ki damage per stack of {}. Lasts **2 turns**.\nThe maximum {} stacks is increased by **2**, they stacks up **2x** faster and their duration is increased by **1**.').format(Acid().icon, Acid().icon, Acid().icon)
        
        return

    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        '''
        `coroutine`

        Applies the Unity is strenght buff, increase all acid max stack, and duration by 1
        '''

        # Init

        caster.flag = 1

        # Applies the buff on the whole team
        # If they already have the buff, we reset the duration

        # Check if the character has the buff
        new_buff = Unity_is_strenght()  # New buff instance per character
        has_buff = await Has_buff(caster, Unity_is_strenght())

        if has_buff:
            # get the buff
            char_buff = await Get_buff(caster, Unity_is_strenght())

            # Remove the buff and replace it
            caster.buff.remove(char_buff)
            caster.buff.append(new_buff)
        
        else:
            caster.buff.append(new_buff)
        
        move += await Display_move(client, ctx, self.name, self.icon, 0, caster, caster, is_ki = True)

        return(move)