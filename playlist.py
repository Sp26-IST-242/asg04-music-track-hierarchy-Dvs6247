"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""

class Playlist:
    def __init__(self):
        # Private field initialized as an empty list
        self._tracks = []

    def add_track(self, track):
        """Appends a MusicTrack to the list. Returns None."""
        self._tracks.append(track)

    def clear_playlist(self):
        """Clears the list using .clear(). Returns None."""
        self._tracks.clear()

    def sort_by_release_year(self):
        """Sorts _tracks in place based on release year."""
        # Assumes MusicTrack object has a 'release_year' attribute
        self._tracks.sort(key=lambda x: x.release_year)

    def __str__(self):
        """Returns each track on its own line."""
        return "\n".join([str(track) for track in self._tracks])

    @property
    def tracks(self):
        """Returns a copy of the internal list (protects encapsulation)."""
        return self._tracks.copy()
    