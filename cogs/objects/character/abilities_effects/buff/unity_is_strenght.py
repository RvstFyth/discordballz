'''
Manages Unity is Strenght buff

Last update: 26/06/19
'''

# Dependancies

import asyncio

# Object
from cogs.objects.class_referencer import Get_class
from cogs.objects.character.abilities_effects.buff._buff_object import Buff

# Utils

from cogs.utils.functions.commands.fight.functions.effect.replace_effect import Replace_dot
from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_dot
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_dot


class Unity_is_strenght(Buff):

    # Class attribute

    name = 'Unity is strenght'
    id = 1
    icon = '<:unity_is_strenght:585503883133059074>'

    # Instance attributes

    def __init__(self):
        Buff.__init__(self)
        
        # Init
        self.duration = 2
        self.max_stack = 1
        self.stack = 1
    
    async def apply(self, client, ctx, target, player_team, enemy_team):
        '''
        `coroutine`

        Heal up the character for each active Acid satck.
        '''

        # Init

        has_acid = False
        acid_stacks = 0
        acid_ = None
        healing = 0

        # class
        acid_ = await Get_class(1)
        acid_ = acid_()

        # Find there is acid
        # If acid found, increase acid_stacks counter
        # also increase their duration and max stack

            # Player team
        for character in player_team:
            await asyncio.sleep(0)

            # Test if the character has acid 
            has_acid = await Has_dot(character, acid_)

            if has_acid:  # If he does
                acid_ = await Get_dot(character, acid_)
                acid_stacks += acid_.stack  # Increase acid stack count

                # Increase the max stack and duration

                acid_.max_stack = 5
                acid_.initial_duration = 5
                await Replace_dot(character, acid_)
        
            # Enemy team
        for enemy in enemy_team:
            await asyncio.sleep(0)

            has_acid = await Has_dot(enemy, acid_)

            if has_acid:
                acid_ = await Get_dot(enemy, acid_)
                acid_stacks += acid_.stack

                # Increase the max stack and duration

                acid_.max_stack = 5
                acid_.initial_duration = 5

                await Replace_dot(character, acid_)
        
        # Apply the effect
        if(acid_stacks > 0):  # If there is at least one acid stack active
            healing = acid_stacks*(0.1*target.ki_damage_max)
            target.current_hp += int(healing)

            if(target.current_hp > target.max_hp):
                target.current_hp = target.max_hp
            
        return(int(healing))