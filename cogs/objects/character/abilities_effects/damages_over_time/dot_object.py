'''
Manages the DoT object.

Last update: 24/05/19
'''

class Dot:
    '''
    Represent a damage over time effect.

    Attributes :
        Class :
        - effect_type
        - effect_description
    
        Instance :
        - init_duration : int
        - current_duration : int
        - total_damage : int
        - tick_damage : int
        - max_stack : int
        - stack : int
    '''
    # Class attributes

    effect_type = 'dot'
    effect_description = 'Inflict damage over time.'

    # Instance attributes

    def __init__(self):
        # Duration
        self.init_duration = 0
        self.current_duration = 0

        # Stacks
        self.max_stack = 0
        self.stack = 0

        # Damages
        self.total_damage = 0
        self.tick_damage = (self.total_damage/self.init_duration)*self.stack
    
    # Method

    async def apply_dot(self, target):
        pass