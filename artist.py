"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""

class Artist:
    
    def __init__(self, name: str, genre: str):
        '''
        Initializes the Artist with a name and genre.
        '''
        self._name = name
        self._genre  = genre

        @property
        def name(self) -> str:
          '''The artist or show name.'''
          return self._name
        
        @property
        def __str__(self) -> str:
           '''
           Returns a string representation: <name>, <genre>
           '''
           return f"{self._name}, {self._genre}"
        
        #Example:
        #artist = Artist("Kendrick Lamar", "Hip-Hop")
        #print(artist)
        #print(artist.name)