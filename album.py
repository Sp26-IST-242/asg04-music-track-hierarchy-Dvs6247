"""
Represents a music album or podcast series, including the years it was active.

Key concepts to implement:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""

class Album:
    def __init__(self, title: str, active: bool, years: list[int]):
        """Initializes Album, ensuring years list is not empty and protected."""
        if not years:
            raise ValueError("The 'years' list cannot be empty.")
        
        self._title = title
        self._active = active
        # Defensive copy to prevent external mutation
        self._years = list(years) 

    @property
    def title(self) -> str:
        return self._title

    @property
    def active(self) -> bool:
        return self._active

    @property
    def years(self) -> list[int]:
        # Return a copy to keep internal list private
        return list(self._years)

    @property
    def debut_year(self) -> int:
        """Returns the first year in the list as the debut year."""
        return self._years[0]

    def __str__(self) -> str:
        """Returns string representation: <title> active = <bool>, debut year: <year>"""
        return f"{self._title} active = {self._active}, debut year: {self.debut_year}"

#Example: 
#album = Album("DAMN.", True, [2017, 2018])
#print(album)
#The output comes out as DAMN. active = True, debut year = 2017