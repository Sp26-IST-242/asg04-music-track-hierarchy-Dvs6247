"""
Abstract base class for all music tracks (Songs and Podcasts).

Design decisions to implement:
  • ABC makes it impossible to instantiate MusicTrack directly — you can only
    create concrete subclasses that implement every @abstractmethod.
  • Common fields (artist, album, duration_seconds) live here so that Song and
    Podcast do not each need to repeat them.
  • release_year is a *derived* property delegating to Album.debut_year; the
    year is not stored a second time.
  • play_time_formatted() is abstract because Song and Podcast format time
    differently (MM:SS vs HH:MM:SS).
  • total_play_time() is concrete because the calculation is identical for all
    track types: duration × number of plays.
  • @functools.total_ordering generates <=, >, >= automatically from __eq__ and
    __lt__, giving us full comparison support with minimal code.
  • __hash__ is defined to stay consistent with __eq__ (Python sets __hash__ to
    None when you define __eq__, making objects unhashable unless you fix it).
"""

from abc import ABC, abstractmethod

class MusicTrack(ABC):
    """
    Abstract base class for musical tracks, identifying common fields 
    between Song and Podcast subclasses.
    """
    def __init__(self, title: str, duration_seconds: float, album):
        self._title = title
        self._duration_seconds = duration_seconds
        self._album = album

    @property
    def title(self) -> str:
        return self._title

    @property
    def duration_seconds(self) -> float:
        return self._duration_seconds

    @property
    def album(self):
        return self._album

    @property
    def release_year(self) -> int:
        """
        Returns the track's debut year derived from the Album's years list.
        Assumes the Album object has a 'years' attribute (list of ints).
        """
        return min(self._album.years)

    @abstractmethod
    def play_time_formatted(self) -> str:
        """Returns a human-readable string representation of the track's duration."""
        pass

    def total_play_time(self, num_plays: int) -> float:
        """Returns the total duration in seconds for a given number of plays."""
        return self._duration_seconds * num_plays
