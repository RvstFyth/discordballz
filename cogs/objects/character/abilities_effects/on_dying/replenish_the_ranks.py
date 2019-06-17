'''
Manages the dying object of replenish the ranks.

Last update: 16/06/19
'''

# dependancies

import asyncio

# objects

from cogs.objects.character.characters_list.all_char import Get_char
from cogs.objects.character.abilities_effects.on_dying._on_dying_object import On_Dying

# abilities

from cogs.objects.character.abilities.offensive.ability_acid import Ability_Acid

class Dying_ReplenishTheRanks(On_Dying):

    name = 'Replenish the Ranks'
    id = 1
    icon = ''

    def __init__(self):
        On_Dying.__init__(self)
        self.resurrect = True
        
    
    async def apply(self, client, ctx, target, team_a, team_b):
        '''
        `coroutine`

        Replace the target by Char_2() if Saibaiman (if its id is in [1,3])

        set the can_resurrect to False

        Return : Char_2() or same object
        '''

        # init
        if(target.can_resurrect):
            replacer = await Get_char(2)
            replacer.level = target.level  # Copy the level of the dead target
            await replacer.init(client, ctx)

            replacer.current_hp = int(0.10*replacer.max_hp)  # Set the HPs  

            # The target can only use Acid

            replacer.ability_list = []
            replacer.ability_list.append(Ability_Acid)

            target = replacer
            target.can_resurrect = False

            return(target)
        
        else:
            return(target)