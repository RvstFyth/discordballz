'''
Store the character's basic informations using its global id.

Last update: 02/06/19
'''

# Dependancies

import asyncio

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
        - category : int
        - type : int
        - rarity : int
        - rarity_value : int

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
        - ability_count : int

        - has_passive : bool
        - passive_name : str (init to NONE)
        - passive_description : str
        - has_leader : bool
        - leader_name : str (init to NONE)
        - leader_description : str

        - first_ability_name : str
        - first_ability_description : str
        - first_ability_icon : str
        - first_ability_cost : int
        - first_ability_cooldown : int (init to a certain value to avoid player to use an ability at the beginning of the fight)

        - second_ability_name : str
        - second_ability_description : str
        - second_ability_icon : str
        - second_ability_cost : int
        - second_ability_cooldown : int (init to a certain value to avoid player to use an ability at the beginning of the fight)

        - third_ability_name : str
        - third_ability_description : str
        - third_ability_icon : str
        - third_ability_cost : int
        - third_ability_cooldown : int (init to a certain value to avoid player to use an ability at the beginning of the fight)

        - fourth_ability_name : str
        - fourth_ability_description : str
        - fourth_ability_icon : str
        - fourth_ability_cost : int
        - fourth_ability_cooldown : int (init to a certain value to avoid player to use an ability at the beginning of the fight)

        Effects :
        - buff : list
        - debuff : list
        - dot : list

    Methods :
        Init :
        - `coro` : init(client, ctx)
        
        Passives :
        - `coro` : Passive_skill()
        - `coro` : Leader_skill()

        Event :
        - `coro` : On_being_attacked()
        - `coro` : On_being_killed()
        - `coro` : On_attacking()
        - `coro` : On_killing()

        Abilities :
        - `coro` : First_ability()
        - `coro` : Second_ability()
        - `coro` : Third_ability()
        - `coro` : Fourth_ability()
    '''

    # Instance attributes

    def __init__(self):
        # Basic infos
        self.id = 0
        self.name = ''
        self.image = ''  # Image URL
        self.category = 0
        self.type = 0
        self.rarity = 0
        self.rarity_value = 0

        # Variation
        self.level = 0

        # Fight infos
        self.max_hp = 0
        self.current_hp = self.max_hp

        self.max_ki = 0
        self.current_ki = 0

        self.physical_damage_max = 0
        self.physical_damage_min = int(90*(self.physical_damage_max)/100)  # The minimum damages represent 90 % of the max damages
        self.ki_damage_max = 0
        self.ki_damage_min = int(90*(self.ki_damage_max)/100)
        
        self.physical_defense = 0
        self.ki_defense = 0
        self.damage_reduction = 0  # In % : damage_reduction = 1 +/- (dmg_reduction/100)
        
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
        self.ability_count = 0  # Represents the number of abilities a character has

        self.has_passive = False  # True if the character has a passive ability
        self.passive_name = None  # None if it has no name, string if it has one
        self.passive_description = ''

        self.has_leader = False  # True if the character has a leader skill
        self.leader_name = None
        self.leader_description = ''

        self.first_ability_name = ''
        self.first_ability_description = ''
        self.first_ability_icon = ''
        self.first_ability_cost = 0
        self.first_ability_cooldown = 0

        self.second_ability_name = ''
        self.second_ability_description = ''
        self.second_ability_icon = ''
        self.second_ability_cost = 0
        self.second_ability_cooldown = 0

        self.third_ability_name = ''
        self.third_ability_description = ''
        self.third_ability_icon = ''
        self.third_ability_cost = 0
        self.third_ability_cooldown = 0

        self.fourth_ability_name = ''
        self.fourth_ability_description = ''
        self.fourth_ability_icon = ''
        self.fourth_ability_cost = 0
        self.fourth_ability_cooldown = 0

    # Methods

    async def init(self, client, ctx):
        pass
    
    # Passives

    async def Passive_skill(self):
        pass
    
    async def Leader_skill(self):
        pass

    # On event

    async def On_being_attacked(self):
        pass
    
    async def On_being_killed(self):
        pass
    
    async def On_attacking(self):
        pass
    
    async def On_killing(self):
        pass

    # Abilities

    async def First_ability(self):
        pass
    
    async def Second_ability(self):
        pass
    
    async def Third_ability(self):
        pass
    
    async def Fourth_ability(self):
        pass