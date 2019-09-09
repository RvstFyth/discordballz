"""
Manages the health attribute of a character.

--

Author : DrLarck

Last update : 09/09/19 (DrLarck)
"""

# character health
class Character_health:
    """
    Manages the character's health attribute.

    - Attribute :

    `maximum` : Represents the character's maximum health.

    `current` : Represents the character's current health amount.

    - Method :

    :coro:`health_limit()` : Set the health limit, if current > max, current = max, else if current < 0, current = 0.
    """

    # attribute
    def __init__(self):
        self.maximum = 0
        self.current = 0
        self.regen = 0
    
    # method
    async def health_limit(self):
        """
        `coroutine`

        Set the health limit. If the character's current health is higher than its maximum, set the current health to max.

        Else, if the character's current health is negative, set it to 0.

        --

        Return : None
        """

        # greater than max
        if(self.current > self.maximum):
            self.current = self.maximum
            return
        
        if(self.current < 0):
            self.current = 0
            return