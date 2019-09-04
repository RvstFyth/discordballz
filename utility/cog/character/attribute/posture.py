"""
Manages the character's posture.

--

Author : DrLarck

Last update : 04/09/19 (DrLarck)
"""

# class posture
class Character_posture:
    """
    Manages the character's posture.

    - Attribute :

    Each attribute represents a character posture.

    `attacking` (bool) : Default to `True`
    
    `defending` (bool)

    `charging` (bool)

    `stunned` (bool)

    `ghost` (bool) : Tells if a character can be resurrected or not. If false, the character can be resurrected.

    - Method :

    :coro:`get_posture()` : Returns the posture name and icon.

    :coro:`change_posture(posture)` : Changes the character's posture to the passed posture. The posture must be passed as 
    str.
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
    async def get_posture(self):
        """
        `coroutine`

        Return the character's posture name and icon.

        --

        Return : posture name, icon
        """

        # init
        posture = None
        icon = None

        if(self.attacking):
            posture = "Attacking"
            icon = ":crossed_swords:"
        
        elif(self.defending):
            posture = "Defending"
            icon = ":shield:"
        
        elif(self.charging):
            posture = "Charging"
            icon = ":fire:"
        
        elif(self.stunned):
            posture = "Stunned"
            icon = ":dizzy_face:"
        
        return(posture, icon)

    async def change_posture(self, posture):
        """
        `coroutine`

        Changes the character's posture.

        - Parameter :

        `posture` : Represents the new character posture as `str`. I.e supported posture.

        Supported posture :
        - attacking
        - defending
        - charging
        - stunned
        """
        
        self.attacking = False
        self.defending = False
        self.charging = False
        self.stunned = False

        if(posture.lower() == "attacking"):
            self.attacking = True
            return
        
        elif(posture.lower() == "defending"):
            self.defending = True
            return
        
        elif(posture.lower() == "charging"):
            self.charging = True
            return
        
        elif(posture.lower() == "stunned"):
            self.stunned = True
            return
        
        else:
            print(f"(CHANGE POSTURE) Error : Posture not found : {posture}")
            return