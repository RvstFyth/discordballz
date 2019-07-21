"""
Manages the character's damage attribute.

-- 

Author : DrLarck

Last update : 18/07/19
"""

# damage attribute
class Character_damage:
    """
    Manages the character's damage attribute.

    - Attribute :

    `physical_max` | `physical_min` : Represents the max physical damage and min.

    `ki_max` | `ki_min` : Same as physical, but for ki abilities.
    """

    # attribute
    def __init__(self):
        # physical damage values
        self.physical_max = 0
        self.physical_min = 0

        # ki damage values
        self.ki_max = 0
        self.ki_min = 0