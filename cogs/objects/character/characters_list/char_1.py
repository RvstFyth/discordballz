'''
Manage the character_1

Last update: 26/06/19
'''

# Dependancies

import asyncio
from random import randint

# Objects

from cogs.objects.character.character import Character

# Abilities

from cogs.objects.character.abilities_effects.damages_over_time.acid import Acid
from cogs.objects.character.abilities.offensive.ability_acid import Ability_Acid
from cogs.objects.character.abilities.offensive.ability_syphon import Ability_Syphon
from cogs.objects.character.abilities.support.ability_unityIsStrenght import Ability_UnityIsStrenght
from cogs.objects.character.abilities_effects.buff.unity_is_strenght import Unity_is_strenght

# Utils

from cogs.utils.functions.commands.fight.functions.stat_manager import Set_stat
from cogs.utils.functions.commands.fight.displayer.display_move import Display_move
from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon, Get_type_icon
from cogs.utils.functions.translation.gettext_config import Translate
from cogs.utils.functions.commands.fight.functions.damage_calculator import Damage_calculator

from cogs.utils.functions.readability.displayer.saga_displayer import Get_Saga

# Ai
from cogs.utils.functions.commands.fight.functions.effect.get_effect import Get_dot
from cogs.utils.functions.commands.fight.functions.effect.has_effect import Has_dot

class Char_1(Character):
    '''
    Represents : `Green Saibaiman`

    The stats are based on the lv.1
    '''

    # Instance attributes

    def __init__(self):
        Character.__init__(self)
        # Basic
        self.level = 150
        self.id = 1
        self.name = 'Green Saibaiman'
        self.image = 'https://i.imgur.com/1m8rA7L.png'
        self.thumb = 'https://i.imgur.com/SITD9VY.png'
        self.icon = '<:saibaiman_a:589485375685263373>'
        self.saga = 0
        self.type_icon = 0
        self.type_value = 0
        self.rarity_icon = 0
        self.rarity_value = 5

        # Fight
        self.max_hp = 3500
        self.current_hp = 3500
        self.max_ki = 100
        self.current_ki = 0

        self.physical_damage_max = 400
        self.physical_damage_min = 360  # The minimum damages represent 90 % of the max damages (90*max)/100 ou 0.9*max
        self.ki_damage_max = 850
        self.ki_damage_min = 765

        self.physical_defense = 475
        self.ki_defense = 400
        self.critical_chance = 10  # In %
        self.dodge_chance = 10  # In %
        self.ki_regen = 2
        self.health_regen = 0

        self.dot = []
        self.debuff = []
        self.buff = []

        # Abilities
        self.ability_list = [Ability_Acid, Ability_Syphon, Ability_UnityIsStrenght]  # Represents the number of abilities a character has

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

        self.name = _('Green Saibaiman')
        self.saga = await Get_Saga(client, ctx, self)

        # Icons

        self.rarity_icon = await Get_rarity_icon(self.rarity_value)
        self.type_icon = await Get_type_icon(self.type_value)

        # Set stats

        await Set_stat(client, ctx, self)
        return

    # Abilities

    async def Use_ability(self, client, ctx, caster, target, team_a, team_b, move: str, ability):
        '''
        `coroutine`
        '''

        # Init

        get_ability = self.ability_list[ability]
        ability_ = get_ability()
        
        await ability_.init(client, ctx, caster)

        return(ability_)
    
    # AI

    async def artificial_intelligence(self, client, ctx, caster, npc_team, enemy_team):
        '''
        `coroutine`

        We want the Green Saibaiman to stack acid on the target which has the highest amount 

        of maximum health.

        Once a target has reached 3 stacks, Saibaiman wether choose to use Unity is Strenght to stack

        up to 5 stacks on the target, then Syphon it, or to syphon directly with 3 stacks

        If the target has less Ki defense than Armor the Saibaiman will always choose to charge his ki

        to maximize his Ki damages.
        '''

        # init
        # Get the target with the highest amount of health (max)
        # always focus the target with the highest amount of hps
        
        move = 0
        tankiest = enemy_team[0]  # init to the first char
        random_target = enemy_team[randint(0, len(enemy_team)-1)]
        target = None

        for enemy in enemy_team:
            await asyncio.sleep(0)

            if(enemy.current_hp > 0):  # need to be alive
                if(enemy.max_hp > tankiest.max_hp):  # If the current enemy has more HP than the previous tankiest, take his place
                    tankiest = enemy
                
                else:  # not tankiest
                    pass
            
            else:  # not alive
                pass
        
        if(self.current_ki >= self.ability_list[0]().cost):  # if has enough ki to launch acid
            # check the amount of acid stack on the target
            has_acid = await Has_dot(tankiest, Acid())

            if has_acid:
                acid_ = await Get_dot(tankiest, Acid())

                # If the target has more than 50 % of his maximum health
                # and has 3 stacks of acid, we search to use Unity is strenght and stack
                # more acid on it
                if(acid_.stack >= acid_.max_stack):  # If the target has reached the acid max stacks
                    if(tankiest.current_hp > (tankiest.max_hp)/2):  # If the target has more than 50 % of its max hp
                        # Then we decide to use unity is strenght or to charge Ki to use it
                        if(self.current_ki >= self.ability_list[1]().cost):
                            if(self.current_ki >= self.ability_list[2]().cost):  # if I have enough ki to use Unity is strenght
                                move = randint(5, 6)  # -3 = 2 so ability[2] = Unity is strebnght
                                target = tankiest

                            else:
                                move = randint(1, 5)
                                target = tankiest
                        
                        else:  # if not enought ki to use
                            move = randint(1, 3)  # then ki charge

                            target = random_target
                    
                    else:  # target has 3 stacks of acid and more less 50 % of hp
                        if(self.current_ki >= self.ability_list[1]().cost):  # if enough ki to use syphon
                            move = 5  # use syphon

                            target = tankiest
                        
                        else:
                            move = randint(1, 3)  # else charge

                            target = random_target
                
                elif(acid_.stack < acid_.max_stack):  # if acid stack are not max
                    if(self.current_ki >= self.ability_list[0]().cost):  # if enouth ki to acid
                        move = 4
                        target = tankiest
                    
                    else:  # else charge
                        move = randint(1, 3)

                        target = random_target

            else:  # doesn't have acid stack on him
                # we want to stack up acid
                if(self.current_ki >= self.ability_list[0]().cost):
                    move = 4

                    target = tankiest
                
                else:  # charge or dps or defend
                    move = randint(1, 3)

                    target = random_target

        else:  # if not enough ki to launch acid
            # randomly do something
            move = randint(1, 3)

            target = random_target
        
        # END
        if(move == 2):  # No target if charging
            target = None
        
        if(move == 3):
            target = None
    
        decision = [move, target]
        return(decision)