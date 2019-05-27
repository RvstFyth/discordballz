'''
Manage the character_1

Last update: 24/05/19
'''

# Dependancies

import asyncio

# Objects

from cogs.objects.character import Character
from configuration.characters.abilities_effects.damages_over_time.acid import Acid

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

class Char_1(Character):
    '''
    Represents : `Saibaiman`

    The stats are based on the lv.1

    `target` : must be `Character` or `Enemy` object.

    `player_team` : must be list of `Character` objects.

    `enemy_team` : must be list of `Enemy` objects.
    '''

    # Instance attributes

    def __init__(self):
        # Basic
        self.name = 'Saibaiman'
        self.image = 'https://i.imgur.com/1m8rA7L.png'
        self.category = 0
        self.type = 0
        self.rarity = 0

        # Fight
        self.max_hp = 3500
        self.current_hp = self.max_hp
        self.max_ki = 100
        self.current_ki = self.max_ki
        self.damage_max = 850
        self.damage_min = int(90*(self.damage_max)/100)  # The minimum damages represent 90 % of the max damages
        self.defense = 700
        self.critical_chance = 10  # In %
        self.dodge_chance = 10  # In %
        self.ki_regen = 2
        self.health_regen = 0

        # Abilities
        self.ability_count = 1  # Represents the number of abilities a character has

        self.first_ability_name = 'Acid'
        self.first_ability_description = '''
Applies a stack of **Acid** on the target. Each stack of **Acid** deals an amount of *2 %* of the target's maximum health as damages per turn.
Ignore the target defense.'''

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

        self.name = _('Saibaiman')

        # Ability 

        self.first_ability_name = _('Acid')
        self.first_ability_description = _('Applies a stack of **Acid** on the target. Each stack of **Acid** deals an amount of *2 %* of the target\'s maximum health as damages per turn.Ignore the target defense.')

    # Abilities

    async def first_ability(self, client, ctx, target, player_team, enemy_team):
        '''
        `coroutine`

        `enemy` : Must be `Enemy` object.
        '''

        # Init Acid damages

        acid_dot, identical = Acid(), False
        acid_dot.duration, acid_dot.stack = 10, 1  # Set the duration and the stacks

        acid_dot.total_damage = (2*target.stat.max_hp)/100  # Set the damages
        acid_dot.tick_damage = int((acid_dot.total_damage/acid_dot.duration)*acid_dot.stack)

        for Dot in target.dot :  # We check all the dot the target has
            await asyncio.sleep(0)

            if Dot.dot_name == acid_dot.dot_name :  # If we find the same Dot we copy it
                identical = True
                acid_dot = Dot
                target.dot.remove(Dot)  # We remove the old Dot and apply a new one

                if(acid_dot.stack < acid_dot.max_stack):  # If we haven't reached the max stacks we ad another one
                    acid_dot.stack += 1

                target.dot.append(acid_dot)  # Apply the new dot

                break
        
        if not identical :  # If we don't find the dot into the Target dots list we add it
            target.dot.append(acid_dot)