"""
Manages the character's self regeneration.

--

Author : DrLarck

Last update : 18/07/19
"""

# charcter regen
class Character_regen:
    """
    Manages the character's self regeneration.

    - Attribute :

    `health` : Represents the health regen per turn.

    `ki` : Represents the ki regen per turn.
    """

    # attribute
    def __init__(self):
        self.health = 0
        self.ki = 0