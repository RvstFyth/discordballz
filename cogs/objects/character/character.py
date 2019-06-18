'''
Store the character's basic informations using its global id.

Last update: 18/06/19
'''

# Dependancies

import asyncio
from random import randint

# Utils

from cogs.utils.functions.translation.gettext_config import Translate

class Character:
    '''
    Represent a character.

    Attributes :
        Basic
        - id : int
        - name : str
        - image : str (url)
        - saga : int
        - type : int
        - rarity : int
        - rarity_value : int

        Variation
        - level : int
            Enhancement
            - star : 0
            - training_item_health : int (represent the number of training item used)
            - training_item_physical_damage : int
            - training_item_ki_damage : int
            - training_item_physical_defense : int
            - training_item_ki_defense : int

        Fight
        - max_hp : int
        - current_hp : int

        - max_ki : int
        - current_ki : int

        - physical_damage_max : int
        - physical_damage_min : int
        - ki_damage_max : int
        - ki_damage_min : int

        - physical_defense : int
        - ki_defense : int
        - damage_reduction : int (%)

        - critical_chance : int (%)
        - critical_bonus : int (%)
        - dodge_chance : int (%)

        - ki_regen : int
        - health_regen : int

        - flag : int (0 atk, 1 charging, 2 def, 3 stun)

        Abilities :
        - ability_list : list of object `Ability()`

        - has_passive : bool
        - passive_name : str (init to NONE)
        - passive_description : str

        - has_leader : bool
        - leader_name : str (init to NONE)
        - leader_description : str

        Effects :
        - buff : list
        - debuff : list
        - dot : list

        Specials :
        - being_attacked_triggered : bool
        - being_killed_triggered : bool
        - attacking_triggered : bool
        - killing_triggered : bool

    Methods :
        Init :
        - `coro` : init(client, ctx)
        
        Passives :
        - `coro` : Passive_skill(receiver, team_a, team_b)
        - `coro` : Leader_skill(receiver, team_a, team_b)

        Event :
        - `coro` : On_being_attacked(receiver, team_a, team_b)
        - `coro` : On_being_killed(receiver, team_a, team_b)
        - `coro` : On_attacking(receiver, team_a, team_b)
        - `coro` : On_killing(receiver, team_a, team_b)

        Abilities :
        - `coro` : Use_ability(self, client, ctx, caster, target, team_a, team_b, move: str, ability: )
    '''

    # Instance attributes

    def __init__(self):
        # Basic infos
        self.id = 0
        self.name = ''
        self.image = ''  # Image URL
        self.icon = ''
        self.saga = 0
        self.type_icon = 0
        self.type_value = 0
        self.rarity_icon = 0
        self.rarity_value = 0

        # Variation
        self.level = 0

            # Enhancement
        self.star = 0  # Number of stars (up to 5)
        self.training_item_health = 0  # Number of training items used 
        self.training_item_physical_damage = 0
        self.training_item_ki_damage = 0
        self.training_item_physical_defense = 0
        self.training_item_ki_defense = 0

        # Fight infos
        self.max_hp = 0
        self.current_hp = 0

        self.max_ki = 0
        self.current_ki = 0

        self.physical_damage_max = 0
        self.physical_damage_min = 0 # The minimum damages represent 90 % of the max damages
        self.ki_damage_max = 0
        self.ki_damage_min = 0
        
        self.physical_defense = 0
        self.ki_defense = 0
        self.damage_reduction = 0  # In % : damage_reduction = 1 +/- (dmg_reduction/100), if > 0 = takes more damages, else, reduce damages
        
        self.critical_chance = 0 # In %
        self.critical_bonus = 0  # In % represent the critical damages bonus
        self.dodge_chance = 0  # In %

        self.ki_regen = 0
        self.health_regen = 0

        self.flag = 0  # 0 : Attack, 1 : Charge, 2 : Def, 3 : stun

        # Effects handlers
        self.buff = []
        self.debuff = []
        self.dot = []

        # Abilities infos
        self.ability_list = []  # Contains the list of abilities
        self.passive_list = []  # Contains all the passive abilities
        self.leader_list = []  # Contains all the leader skill abilities

        self.while_attacked = []  # Contains all the behaviour on being attacked
        self.while_attacking = []  # Same but when this character attacks

        self.dying = []  # Do something when dying
        self.while_dead = []  # Do something while dead

        self.can_resurrect = True  # If false, the character cant be resurrected

        # Sepcials

        self.being_attacked_triggered = False
        self.being_killed_triggered = False
        self.attacking_triggered = False
        self.killing_triggered = False

    # Methods

    async def init(self, client, ctx):
        pass
    
    async def inflict_damage(self, client, ctx, attacker, damage, team_a, team_b):
        '''
        `coroutine`

        Reduce the current health in function of the damages received.

        If the character dies, trigger all the self.dying effects.

        `attacker` : represents the character who is attacking.

        `damage` : must be type `int`.

        `team_a` : represents the player team

        `team_b` : represents the enemy team
        '''

        # init

        if(self.current_hp > 0):  # Only applies the changes if the character is alive
            gonna_die = False  # tell if the character is gonna die or not

            # receive damages

            if(damage >= self.current_hp):  # If the damages are too high it means the char is just gonna die
                gonna_die = True

            self.current_hp -= damage 

            # if dies

            if gonna_die:  # If the damages killed the character
                # Trigger the dying effects

                for effect in self.dying:
                    await asyncio.sleep(0)

                    if(effect.resurrect):  # if the on_dying does resurrect a character
                        resurrected = await effect.apply(client, ctx, self, team_a, team_b)
                        await resurrected.init(client, ctx)

                        self.__dict__.update(resurrected.__dict__)  # change the object
                    
                    else:
                        await effect.apply(client, ctx, self, team_a, team_b)

        return

    def stat_limit(self):
        '''
        Force the stat to 0 if their value is under 0
        '''

        # Health

        if(self.max_hp < 0):
            self.max_hp = 0

        if(self.current_hp < 0):
            self.current_hp = 0
        
        return

    # Abilities

    async def Use_ability(self, client, ctx, caster, target, team_a, team_b, move: str, ability):
        pass
    
    # Triggers

    async def trigger_passive(self, character, team_a, team_b):
        '''
        `coroutine`

        Triggers all the passive in passive list
        '''

        if(len(self.passive_list) > 0):  # if not empty
            for passive in self.passive_list:
                await asyncio.sleep(0)

                passive.trigger(character, team_a, team_b)
        
        return
    
    async def trigger_leader(self, character, team_a, team_b):
        '''
        `coroutine`

        Triggers all the leader skill in leader list
        '''

        if(len(self.leader_list) > 0):  # if not empty
            for leader in self.leader_list:
                await asyncio.sleep(0)

                leader.trigger(Character, team_a, team_b)
        
        return
    
    # AI

    async def artificial_intelligence(self, client, ctx, caster, npc_team, enemy_team):
        '''
        `coroutine`

        Manages the basic artificial intellignece of characters. Please note that 

        `npc_team` represent the `enemy_team`, it's the ally team of this npc.

        `enemy_team` is `player_team`, but represents the enemy team of this npc.

        Return: list[move[1;len(ability_list)], target]
        '''

        # First the check the highly ability cost

        match = False
        ability_id = 0

        move, target = 1, None

        if(self.current_ki >= self.ability_list[len(self.ability_list)-1]().cost):  # If i have enough ki to launch the most expensive ability
            move = randint(1, len(self.ability_list)+1)  # +1 because we also count ki_charge that is '2'

        if(self.ability_list[len(self.ability_list)-1]().need_target):
            target = enemy_team[randint(0, len(enemy_team)-1)]  # Pick a random target

            while target.current_hp <= 0:
                await asyncio.sleep(0)

                target = enemy_team[randint(0, len(enemy_team)-1)]

        else:  # If we don't have max ki, just check all the ability and launch random
            for ability in self.ability_list:
                await asyncio.sleep(0)

                ability = ability()

                if(self.current_ki >= ability.cost):
                    move = randint(1, ability_id+3)  # +3 because the list starts at 0 and we count seqsuence and ki

                    if(move > 2):  # If move is an ability
                        match = True

                        if(ability.need_target):
                            target = enemy_team[randint(0, len(enemy_team)-1)]

                            while target.current_hp <= 0:
                                await asyncio.sleep(0)
                                
                                target = enemy_team[randint(0, len(enemy_team)-1)]
                
                if(match):  # If we have found an ability to use, we go out
                    break

                ability_id += 1
            
            if not match:  # If we have not found any ability to launch, do sequence or charge ki
                move = randint(1, 2)

                if move == 1:  # If sequence
                    target = enemy_team[randint(0, len(enemy_team)-1)]

                    while target.current_hp <= 0:
                        await asyncio.sleep(0)
                        
                        target = enemy_team[randint(0, len(enemy_team)-1)]
        
        if(move == 2):
            target = None
            
        decision = [move, target]
        return(decision)