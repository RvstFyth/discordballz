"""
Manages the character's type attribute.

--

Author : DrLarck

Last update : 18/08/19 (DrLarck)
"""

# class type
class Character_type:
    """
    Manages the character's type attribute.

    - Attribute :

    `icon` : Represents the character's type icon (emoji).

    `value` : Represents the character's type value (0 to 4)
    """

    # attribute
    def __init__(self):
        self.icon = None
        self.value = 0