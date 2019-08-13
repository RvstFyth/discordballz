"""
Manages the character's ki attribute.

-- 

Author : DrLarck

Last update : 13/08/19 (DrLarck)
"""

# ki managment
class Character_ki:
    """
    Manages the character's ki attribute.

    - Attribute :

    `maximum` : Represents the maximum Ki, default set to 100.

    `current` : Represents the current character's ki amount.

    - Method :
    
    :coro:`ki_limit()` : Set the ki limit.
    """

    # attribute
    def __init__(self):
        self.maximum = 100
        self.current = 100
    
    # method
    async def ki_limit(self):
        """
        `coroutine`

        Work the same as the `Health.health_limit()` method.

        -- 

        Return : None
        """

        if(self.current > self.maximum):
            self.current = self.maximum
            return
        
        if(self.current < 0):
            self.current = 0
            return