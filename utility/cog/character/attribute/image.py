"""
Manages the character's images.

--

Author : DrLarck

Last update : 31/08/19 (DrLarck)
"""

# class image
class Character_image:
    """
    Manages the character's images.

    - Attribute :

    `image` : Represents the image url of the character.

    `icon` : Represents the character icon (emoji).

    `thumb` : Represents the character thumbnail (url)
    """

    # attribute 
    def __init__(self):
        self.image = "https://imgur.com/eMiHxeP"
        self.icon = None
        self.thumb = "https://imgur.com/eMiHxeP"
        self.expansion = None