'''
Manages the behavour of Syphon ability

Last update: 14/06/19
'''

# Dependancies

import asyncio

# Object

from cogs.objects.character.abilities.ability import Ability
from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid

# Utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move

    # Effects
from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_dot
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_dot

class Ability_Syphon(Ability):
    '''
    Remove all stack of acid from the target, dealing ki damage and heal himself.
    '''

    icon = '<:syphon:585503902846418961>'
    id = 2

    def __init__(self):
        Ability.__init__(self)
        # Bacic
        
        self.name = 'Syphon'
        self.description = ''

        # Config
        self.can_target_ally = False
        self.need_target = True
        self.cost = 25
        self.cooldown = 0

    # Method

    async def init(self, client, ctx, caster):
        '''
        `coroutine`

        Mainly translate stuff.

        `client` : must be `discord.Client` object.

        `ctx` : must be `discord.ext.commands.Context` object.

        `caster` : must be `Character` object of the character who uses the ability.

        Return: void
        '''

        # Init

        _ = await Translate(client, ctx)
        
        # Translation

        self.name = _('Syphon')
        self.description = _('Removes all {} from the target, dealing **2 %** of the target\'s missing health plus **10 %** of your Ki damage and healing yourself for **50 %** of damages dealt.'.format(Acid().icon))
        
        return
    
    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        '''
        `coroutine`

        Remove all acid stacks from the target dealing damage and healing himself.

        Return: move
        '''

        # Init

        _ = await Translate(client, ctx)

        target_missing_hp = target.max_hp - target.current_hp
        damage_done = await Damage_calculator(caster, target, is_ki = True)
        damage_done = int(damage_done*0.1)  # Inflict 10 % of the ki damage

        # Now we get the acid stacks

        has_acid = await Has_dot(target, Acid())

        if has_acid:  # If the target has acid stack
            # Get the acid dot
            acid_ = await Get_dot(target, Acid())
            damage_done += int(((2*target_missing_hp)/100)*acid_.stack)

            # Now remove acid
            target.dot.remove(acid_)

        # Now heal the caster 
        healing = int(damage_done/2)  # 50 % damages

        # Now deal damage and heal

        await target.inflict_damage(client, ctx, caster, damage_done, team_a, team_b)

        caster.current_hp += healing
        
        if(caster.current_hp > caster.max_hp):
            caster.current_hp = caster.max_hp

        move += _('__Move__ : `{}`{}\n__Damages__ : **-{:,}**:rosette:\n__Heal__ : **+{:,}**:hearts:\n__Ki gain__ : {:,}\n__Ki remaining__ : {:,} / {:,}\n\n').format(self.name, self.icon, damage_done, healing, caster.ki_regen+0, caster.current_ki, caster.max_ki)
        
        return(move)