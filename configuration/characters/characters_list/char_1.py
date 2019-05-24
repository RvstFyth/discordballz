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

    def __init__(self, target, player_team, enemy_team):
        # Basic
        self.name = 'Saibaiman'
        self.image = ''
        self.category = 0
        self.type = 0
        self.rarity = 0

        # Fight
        self.max_hp = 3500
        self.current_hp = self.max_hp
        self.max_ki = 100
        self.current_ki = self.max_ki
        self.damage_max = 850
        self.damage_min = 90*(self.damage_max)/100  # The minimum damages represent 90 % of the max damages
        self.defense = 700
        self.critical_chance = 10  # In %
        self.dodge_chance = 10  # In %
        self.ki_regen = 2
        self.health_regen = 0

        # Targets
        self.target = target
        self.player_team = player_team
        self.enemy_team = enemy_team

        # Abilities
        self.ability_count = 1  # Represents the number of abilities a character has

        self.first_ability_name = 'Acid'
        self.first_ability_description = '''
Applies a stack of **Acid** on the target. Each stack of **Acid** deals an amount of *2 %* of the target's maximum health as damages per turn.
Ignore the target defense.'''

    # Abilities

    async def first_ability(self):
        '''
        `coroutine`

        `enemy` : Must be `Enemy` object.
        '''

        # Translation

        _ = await Translate

        # Ability 

        self.first_ability_name = await _(self.first_ability_name)
        self.first_ability_description = await _(self.first_ability_description)

        # Init Acid damages

        acid_dot, identical = Acid(), False
        acid_dot.init_duration, acid_dot.stack = 4, 1  # Set the duration and the stacks

        acid_dot.total_damage = (2*self.target.max_hp)/100  # Set the damages

        for Dot in self.target.dot :  # We check all the dot the target has
            await asyncio.sleep(0)

            if Dot.dot_name == acid_dot.dot_name :  # If we find the same Dot we copy it
                identical = True
                acid_dot = Dot
                self.target.dot.remove(Dot)  # We remove the old Dot and apply a new one

                if(acid_dot.stack < acid_dot.max_stack):  # If we haven't reached the max stacks we ad another one
                    acid_dot.stack += 1
                
                acid_dot.current_duration = acid_dot.init_duration  # We reset the duration

                self.target.dot.append(acid_dot)  # Apply the new dot

                break
        
        if not identical :  # If we don't find the dot into the Target dots list we add it
            self.target.dot.append(acid_dot)