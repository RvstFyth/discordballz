'''
Manages the effect of the Acid dot.

Last update: 24/05/19
'''

# Dependancies

from configuration.characters.abilities_effects.damages_over_time.dot_object import Dot

class Acid(Dot):
    '''
    Ignore the defense of the target.
    '''

    # Class attribute

    dot_name = 'acid'
    
    # Instance attributes

    def __init__(self):
        # Duration
        self.duration = 4

        # Stacks
        self.max_stack = 3
        self.stack = 0

        # Damages
        self.total_damage = 0
        self.tick_damage = 0
    
    # Method

    async def apply_dot(self, target):
        '''
        `coroutine`
        '''

        if(self.duration > 0):
            if(self.stack >= 3):
                self.tick_damage = int(self.tick_damage * 1.5)  # If there is more than 3 stacks the damages are increased by 50 %
            
            self.duration -= 1
            print(self.tick_damage)

            # Dealing damages

            target.stat.current_hp -= self.tick_damage  # Ignores the defense