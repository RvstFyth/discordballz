'''
Manages the ability Paralyzing burns

Last update : 29/06/19
'''

# dependancies

import asyncio

# object

from cogs.objects.character.abilities.ability import Ability
from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid

from cogs.objects.character.abilities_effects.debuff.paralyzing_burn import Debuff_ParalyzingBurns

# utils

from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move

from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_debuff, Has_dot
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_debuff, Get_dot

class Ability_ParalyzingBurns(Ability):
    
    icon = '<:paralyzing_burns_ki:590183299335323659>'
    id = 7

    def __init__(self):
        Ability.__init__(self)
        self.can_target_ally = False
        self.need_target = True
        self.can_target_enemy = True
        self.name = 'Paralyzing Burns'
        self.description = ''
        self.cost = 75
        self.cooldown = 0
    
    async def init(self, client, ctx, caster):
        '''
        `coroutine`

        Translate
        '''

        _ = await Translate(client, ctx)

        self.name = _('Paralyzing Burns')
        self.description = _('If the target has **at least 3 {}** stacks, the target is **stunned** for **2** turns. If the target has **5 {}** stacks, stuns for **4** turns.\n*Removes all {} stacks*.').format(Acid().icon, Acid().icon, Acid().icon)
        
        return

    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        '''
        `coroutine`

        Stun the target and remove the acid stacks based on the number of stacks.
        '''

        # first check if the target already has the debuff or not

        has_paralyzing = await Has_debuff(target, Debuff_ParalyzingBurns())

        if has_paralyzing:  # Remove the paralyzing debuff
            paralyzing_ = await Get_debuff(target, Debuff_ParalyzingBurns())
            
            await paralyzing_.on_remove(client, ctx, target, team_a, team_b)
            target.debuff.remove(paralyzing_)
        
        else:
            paralyzing_ = Debuff_ParalyzingBurns()

        # Now check if has acid

        has_acid = await Has_dot(target, Acid())

        if has_acid:
            acid_ = await Get_dot(target, Acid())
        
        # Apply the debuff

        if(acid_.stack == 3):
            paralyzing_.duration = 2

            target.debuff.append(paralyzing_)
        
        elif(acid_.stack >= 5):
            paralyzing_.duration = 4

            target.debuff.append(paralyzing_)

        else:
            pass

        move += await Display_move(client, ctx, self.name, self.icon, 0, caster, target)

        return(move)