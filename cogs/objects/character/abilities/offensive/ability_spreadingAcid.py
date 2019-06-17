'''
Manages the spreading acid ability

Last update: 17/06/19
'''

# dependancies

import asyncio

# object

from cogs.objects.character.abilities.ability import Ability
from cogs.objects.character.abilities.offensive.ability_acid import Acid

# utils

from cogs.utils.functions.translation.gettext_config import Translate

from cogs.utils.functions.commands.fight.displayer.display_move import Display_move
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_dot
from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_dot

class Ability_SpreadingAcid(Ability):

    def __init__(self):
        Ability.__init__(self)
        self.can_target_ally = False
        self.need_target = False
        self.name = 'Spreading Acid'
        self.id = 6
        self.icon = '<:spreading_acid_ki:590184731232960523>'
        self.description = ''
        self.cost = 30
        self.cooldown = 0
    
    async def init(self, client, ctx, caster):
        '''
        `coroutine`

        Translate
        '''

        _ = await Translate(client, ctx)

        self.name = _('Spreading Acid')
        self.description = _('All opponents that have {} stacks receive an additional stack.').format(Acid().icon)

        return
    
    async def trigger(self, client, ctx, caster, target, team_a, team_b, move = None, ability = None):
        '''
        `coroutine`

        Check all the opponent, if they have at least one stack of acid, add one stack more.
        '''

        # init

        has_acid = False

        for character in team_b:  # Check all characters in opponent team
            await asyncio.sleep(0)

            has_acid = await Has_dot(character, Acid())

            if has_acid:
                acid_ = await Get_dot(character, Acid())
                character.dot.remove(acid_)

                # Now add a new stack to it

                if(acid_.stack < acid_.max_stack):
                    acid_.stack += 1
                    acid_.duration = 4

                    # New tick damages

                    acid_.tick_damage = int((acid_.total_damage/acid_.duration)*acid_.stack)

                    character.dot.append(acid_)
        
        move += await Display_move(client, ctx, self.name, self.icon, 0, caster, target)

        return(move)