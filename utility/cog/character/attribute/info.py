"""
Manages the .info attribute of the character.

--

Author : DrLarck

Last update : 22/08/19 (DrLarck)
"""

# class info
class Character_info:
    """
    Manages the .info attributes of a character.

    - Attribute : 
    
    `id` : Represents the character's global id.

    `name` : Represents the character's name.

    `saga` : Represents the character's saga name.

    `expansion` : Default 0 
    """

    # attribute
    def __init__(self):
        # basic
        self.id = 0
        self.name = None
        self.saga = None
        self.expansion = 0