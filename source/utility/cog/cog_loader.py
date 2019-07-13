"""
Load the cogs.

--

Author : DrLarck

Last update : 13/07/19 (DrLarck)
"""

class Cog_loader:
    """
    Load the cogs and throw an error in the console if a cog cannot be loaded properly.

    - Parameter : 
    `client` : Represents the `Client`.

    - Attribute :
    `cog` : List of cogs to load.
    `client` : Represents the `Client`.

    - Method :
    `load_cog()` : Loads all the cogs stored in the `cog` attribute.
    """

    # attribute
    def __init__(self, client):
        self.client = client
        self.cog = [
        ]
    
    # method

    def load_cog(self):
        """
        Loads all the cogs stored in the `cog` attribute.
        """

        for cog in self.cog:
            try:
                self.client.load_extension(cog)
            
            except Exception as error:
                print(f"(LOADING COG) - Error while loading {cog} : {error}.")
                pass