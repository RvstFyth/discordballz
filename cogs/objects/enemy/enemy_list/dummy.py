'''
This is the dummy, test everything you want on it.

Last update: 27/05/19
'''

# Dependancies

from cogs.objects.enemy.enemy import Enemy

# Utils

from cogs.utils.functions.readability.displayer.icon_displayer import Get_rarity_icon, Get_type_icon

class Dummy(Enemy):
    '''
    Represents : `Dummy`
    '''

    # Instance attributes

    def __init__(self):
        # Basic infos
        self.id = 1
        self.name = 'Dummy'
        self.image = 'https://i.imgur.com/qNzaU4B.png'  # Image URL
        self.category = 0
        self.type = 0
        self.rarity = 0

        # Variation
        self.level = 0

        # Fight infos
        self.max_hp = 5000000
        self.current_hp = self.max_hp
        self.max_ki = 100
        self.current_ki = self.max_ki
        self.physical_damage_max = 500
        self.physical_damage_min = int(90*(self.physical_damage_max)/100)  # The minimum damages represent 90 % of the max damages
        self.physical_defense = 12
        self.ki_defense = 0
        self.critical_chance = 0 # In %
        self.dodge_chance = 0  # In %
        self.ki_regen = 0
        self.health_regen = 0

        # Abilities infos
        self.ability_count = 0  # Represents the number of abilities a character has
        self.first_ability_name = ''
        self.first_ability_description = ''

        self.second_ability_name = ''
        self.second_ability_description = ''

        self.third_ability_name = ''
        self.third_ability_description = ''

        self.fourth_ability_name = ''
        self.fourth_ability_description = ''

        # Effects
        self.buff = []
        self.debuff = []
        self.dot = []

        # Combat
        self.flag = 0

        # Methods

    async def init(self, client, ctx):
        self.rarity = await Get_rarity_icon(self.rarity)
        self.type = await Get_type_icon(self.type)
        return
    
    # Abilities

    async def first_ability(self):
        pass
    
    async def second_ability(self):
        pass
    
    async def third_ability(self):
        pass
    
    async def fourth_ability(self):
        pass