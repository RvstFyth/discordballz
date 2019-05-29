'''
Store the character's basic informations using its global id.

Last update: 28/05/19
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
    - name : str
    - image : str (url)
    - category : int
    - type : int
    - rarity : int

    Fight
    - max_hp : int
    - current_hp : int
    - max_ki : int
    - current_ki : int
    - damage_max : int
    - damage_min : int
    - defense : int
    - critical_chance : int (%)
    - dodge_chance : int (%)
    - ki_regen : int
    - health_regen : int
    - ability_count : int

    Targets
    - target : Character/Enemy object
    - player_team : List of Character objects
    - enemy_team : List of Enemy objects

    Methods :
    - `coro` init(client, ctx)
    '''

    # Instance attributes

    def __init__(self):
        # Basic infos
        self.name = ''
        self.image = ''  # Image URL
        self.category = 0
        self.type = 0
        self.rarity = 0

        # Fight infos
        self.max_hp = 0
        self.current_hp = self.max_hp
        self.max_ki = 0
        self.current_ki = 0
        self.damage_max = 0
        self.damage_min = int(90*(self.damage_max)/100)  # The minimum damages represent 90 % of the max damages
        self.defense = 0
        self.critical_chance = 0 # In %
        self.dodge_chance = 0  # In %
        self.ki_regen = 0
        self.health_regen = 0

        # Abilities infos
        self.flag = 0  # 0 : Attack, 1 : Charge, 2 : Def
        self.ability_count = 0  # Represents the number of abilities a character has

        self.first_ability_name = ''
        self.first_ability_description = ''
        self.first_ability_cooldown = 0

        self.second_ability_name = ''
        self.second_ability_description = ''
        self.second_ability_cooldown = 0

        self.third_ability_name = ''
        self.third_ability_description = ''
        self.third_ability_cooldown = 0

        self.fourth_ability_name = ''
        self.fourth_ability_description = ''
        self.fourth_ability_cooldown = 0

    # Methods

    async def init(self, client, ctx):
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