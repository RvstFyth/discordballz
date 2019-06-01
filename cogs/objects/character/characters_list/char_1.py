'''
Manage the character_1

Last update: 01/06/19
'''

# Dependancies

import asyncio

# Objects

from cogs.objects.character.character import Character
from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid

# Utils

from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon, Get_type_icon
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
        Character.__init__(self)
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
        self.physical_damage_max = 850
        self.physical_damage_min = int(90*(self.physical_damage_max)/100)  # The minimum damages represent 90 % of the max damages
        self.ki_damage_max = 0
        self.ki_damage_min = int(90*(self.ki_damage_max)/100)
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
        self.first_ability_icon = Acid.dot_icon
        self.first_ability_cost = 8
        self.first_ability_cooldown = 0

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

        # Icons

        self.rarity = await Get_rarity_icon(self.rarity)
        self.type = await Get_type_icon(self.type)

        # Ability 

        self.first_ability_name = _('Acid')
        self.first_ability_description = _('Applies a stack of **Acid** on the target. Each stack of **Acid** deals an amount of *2 %* of the target\'s maximum health as damages per turn.Ignore the target defense.')

    # Abilities

    async def First_ability(self, client, ctx, target, player_team, enemy_team):
        '''
        `coroutine`

        `enemy` : Must be `Enemy` object.
        '''

        # Init Acid damages

        acid_dot, identical = Acid(), False
        initial_duration = 4
        initial_stack = 1

        acid_dot.duration, acid_dot.stack = initial_duration, initial_stack  # Set the duration and the stacks

        acid_dot.total_damage = (2*target.max_hp)/100  # Set the damages
        acid_dot.tick_damage = int((acid_dot.total_damage/acid_dot.duration)*acid_dot.stack)

        for Dot in target.dot :  # We check all the dot the target has
            await asyncio.sleep(0)

            if Dot.dot_name == acid_dot.dot_name :  # If we find the same Dot we copy it
                identical = True
                acid_dot = Dot
                target.dot.remove(Dot)  # We remove the old Dot and apply a new one

                if(acid_dot.stack < acid_dot.max_stack):  # If we haven't reached the max stacks we ad another one
                    acid_dot.stack += 1
                
                acid_dot.duration = initial_duration
                acid_dot.tick_damage = int((acid_dot.total_damage/acid_dot.duration)*acid_dot.stack)

                target.dot.append(acid_dot)  # Apply the new dot

                break
        
        if not identical :  # If we don't find the dot into the Target dots list we add it
            target.dot.append(acid_dot)