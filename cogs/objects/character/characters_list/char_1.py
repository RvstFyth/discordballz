'''
Manage the character_1

Last update: 02/06/19
'''

# Dependancies

import asyncio

# Objects

from cogs.objects.character.character import Character
from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid
from cogs.objects.character.abilities_effects.buff.unity_is_strenght import Unity_is_strenght

# Utils

from cogs.utils.functions.commands.fight.functions.stat_manager import Set_stat
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move
from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon, Get_type_icon
from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator

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
        self.level = 25
        self.id = 1
        self.name = 'Saibaiman'
        self.image = 'https://i.imgur.com/1m8rA7L.png'
        self.category = 0
        self.type = 0
        self.rarity = 0
        self.rarity_value = 0

        # Fight
        self.max_hp = 3500
        self.current_hp = self.max_hp
        self.max_ki = 100
        self.current_ki = self.max_ki

        self.physical_damage_max = 400
        self.physical_damage_min = int(90*(self.physical_damage_max)/100)  # The minimum damages represent 90 % of the max damages
        self.ki_damage_max = 850
        self.ki_damage_min = int(90*(self.ki_damage_max)/100)

        self.physical_defense = 475
        self.ki_defense = 400
        self.critical_chance = 10  # In %
        self.dodge_chance = 10  # In %
        self.ki_regen = 2
        self.health_regen = 0

        # Abilities
        self.ability_count = 3  # Represents the number of abilities a character has

        # Acid
        self.first_ability_name = 'Acid'
        self.first_ability_description = ''
        self.first_ability_icon = Acid().icon
        self.first_ability_cost = 8
        self.first_ability_cooldown = 0

        # Syphon
        self.second_ability_name = 'Syphon'
        self.second_ability_description = ''
        self.second_ability_icon = 'None'
        self.second_ability_cost = 25
        self.second_ability_cooldown = 0

        # Unity is strenght

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

        # Set stats

        await Set_stat(client, ctx, self)

        # Ability 
        # Acid
        self.first_ability_name = _('Acid')
        self.first_ability_description = _('Applies a stack of **Acid** on the target. Each stack of **Acid** deals an amount of *2 %* of the target\'s maximum health as damages per turn.Ignore the target defense.')
        
        # Syphon
        self.second_ability_name = _('Syphon')
        self.second_ability_description = _('Sucks up all **[{}]**{} active stacks on the target dealing **2 %** of target missing health as damage per stacks plus **{:,}** Ki damage, remove all **[{}]**{} acid stacks of the target.\nHeal up for **50 %** of damage dealt.').format(Acid().name, Acid().icon, (0.1*self.ki_damage_max), Acid().name, Acid().icon)

        return

    # Abilities

    async def First_ability(self, client, ctx, target, player_team, enemy_team, move):
        '''
        `coroutine`

        Apply a DoT (Acid) to the target.

        `client` : must be `discord.Client` object.

        `ctx` : must be `discord.ext.commands.Context` object.

        `target` : must be `Character` object.

        `player_team` : must be `list` of `Character` objects.

        `enemy_team` : must be `list` of `Character` objects.

        `move` : must be type `str` and represent the player_team_moves to display the corrects move etc.

        Return: str (player_team_moves)
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

            if Dot.name == acid_dot.name :  # If we find the same Dot we copy it
                identical = True
                acid_dot = Dot
                target.dot.remove(Dot)  # We remove the old Dot and apply a new one

                if(acid_dot.stack < acid_dot.max_stack):  # If we haven't reached the max stacks we ad another one
                    acid_dot.stack += 1
                
                acid_dot.duration = initial_duration
                acid_dot.tick_damage = int((acid_dot.total_damage/acid_dot.duration)*acid_dot.stack)

                target.dot.append(acid_dot)  # Apply the new dot

                break
        
        # Display the move

        damage_done = 0
        
        move += await Display_move(client, ctx, self.first_ability_name, self.first_ability_icon, damage_done, self, target) 
        
        if not identical :  # If we don't find the dot into the Target dots list we add it
            target.dot.append(acid_dot)
        
        return(move)

    async def Second_ability(self, client, ctx, target, player_team, enemy_team, move):
        '''
        `coroutine`

        `client` : must be `discord.Client` object.

        `ctx` : must be `discord.ext.commands.Context` object.

        `target` : must be `Character` object.

        `player_team` : must be `list` of `Character` objects.

        `enemy_team` : must be `list` of `Character` objects.

        `move` : must be type `str` and represent the player_team_moves to display the corrects move etc.

        Return: str (player_team_moves)
        '''

        # Init

        acid = None
        damage_done = 0
        
        for dot in target.dot:  # We're looking for Acid stacks
            await asyncio.sleep(0)

            if(dot.name == Acid().name):  # If we find an acid dot, we go out
                acid = dot
                target.dot.remove(dot)  # Remove the dot as it is consummed
                break
            
            else:
                pass
        
        if not acid == None:  # If we've found an acid Dot
            target_missing_health = target.max_hp - target.current_hp  # Get the missing target health
            damage_per_stack = (2*target_missing_health/100)  # Each consummed stack inflicts 2 % of the missing health
            ki_damage = 0.1*self.ki_damage_max  # We take 10 % of the Ki damage

            damage_done = (damage_per_stack*acid.stack) + ki_damage

            target.current_hp -= int(damage_done)

            if(target.current_hp <= 0):  # If the target is killed we trigget its effect if it has one
                await target.On_being_killed()
            
            else:
                pass
        
        else:
            damage_done = 0.1*self.ki_damage_max
            
            target.current_hp -= damage_done

            if(target.current_hp <= 0):  # If the target is killed we trigget its effect if it has one
                await target.On_being_killed()
            
            else:
                pass
        
        damage_done = int(damage_done)
        move += await Display_move(client, ctx, self.second_ability_name, self.second_ability_icon, damage_done, self, target)
        return(move)
    
    async def Third_ability(self, client, ctx, target, player_team, enemy_team, move):
        '''
        `coroutine`
        '''

        unity = Unity_is_strenght()

        target.buff.append(unity)

        # Display the move

        damage_done = 0
        
        move += await Display_move(client, ctx, self.first_ability_name, self.third_ability_name, damage_done, self, target) 
        
        return(move)