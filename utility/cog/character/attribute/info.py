"""
Manages the .info attribute of the character.

--

Author : DrLarck

Last update : 17/07/19
"""

# class info
class Character_info:
    """
    Manages the .info attributes of a character.

    - Attribute : 
    
    `id` : Represents the character's global id.

    `name` : Represents the character's name.

    `saga` : Represents the character's saga name.
    """

    # attribute
    def __init__(self):
        # basic
        self.id = 0
        self.name = None
        self.saga = None