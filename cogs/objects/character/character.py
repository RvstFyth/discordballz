'''
Store the character's basic informations using its global id.

Last update: 12/06/19
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

        self.has_leader = False  # True if the character has a leader skill
        self.leader_name = None
        self.leader_description = ''

        # Sepcials

        self.being_attacked_triggered = False
        self.being_killed_triggered = False
        self.attacking_triggered = False
        self.killing_triggered = False

    # Methods

    async def init(self, client, ctx):
        pass

    # Abilities

    async def Use_ability(self, client, ctx, caster, target, team_a, team_b, move: str, ability):
        pass