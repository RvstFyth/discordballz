'''
Manages the Acid explosion debuff.

Last update: 15/06/19
'''

# Dependancies

import asyncio

# Object

from cogs.objects.character.abilities_effects.debuff._debuff_object import Debuff
from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid

# Utils

from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_dot
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_dot

class Acid_Explosion(Debuff):

    name = 'Acid Explosion'
    id = 1
    icon = '<:acid_explosion:589512633640550406>'

    def __init__(self):
        Debuff.__init__(self)

        self.duration = 2
        self.max_stack = 1
        self.stack = 1
    
    async def apply(self, target, team_a, team_b):
        '''
        `coroutine`

        Reduce the damage reduction by 2 %
        '''

        # We check if the target has Acid dot
        has_acid = await Has_dot(target, Acid())

        if has_acid:  # If the target has acid active
            # Get the stacks 
            acid_ = await Get_dot(target, Acid())

            stacks = acid_.stack 

            # Reduce the target damage reduction

            target.ki_defense *= (1 - (2/100))*stacks
        
        else:  # Don't do anything if the target doesn't have active acid dot
            return

        return(0)