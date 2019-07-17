"""
Manages the character's posture.

--

Author : DrLarck

Last update : 17/07/19
"""

# class posture
class Character_posture:
    """
    Manages the character's posture.

    - Attribute :

    """

    # attribute
    def __init__(self):
        self.attacking = True
        self.defending = False
        self.charging = False
        self.stunned = False
        
        # special
        self.ghost = False
    
    # method
    async def change_posture(self, attacking = False, defending = False, charging = False, stunned = False):
        """
        `coroutine`

        Changes the character's posture.

        - Parameter :

        `posture` : Represents the new character posture
        """