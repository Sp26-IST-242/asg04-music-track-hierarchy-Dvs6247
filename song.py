"""
Concrete subclass of MusicTrack representing a standard music track.

Song adds no new fields beyond what MusicTrack already stores.  Its only
responsibility is to:
  1. Call super().__init__() to let MusicTrack do the storage work.
  2. Implement play_time_formatted() in MM:SS format.
     Return the duration as 'MM:SS' (both parts zero-padded).

        Examples
        --------
        220 seconds → '03:40'
        65  seconds → '01:05'
        
  3. Override __str__ for a human-readable representation.
     Return '(<artist>) <album>, duration: <MM:SS>'.

        Example:
            (Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017,
            duration: 03:40
"""

class MusicTrack:
    """Represents a general music track."""
    def __init__(self, artist, album, duration_seconds):
        self.artist = artist
        self.album = album
        self.duration_seconds = duration_seconds

class Song(MusicTrack):
    """Represents a specific song, extending MusicTrack."""
    def __init__(self, artist, album, duration_seconds, title):
        # Call super().__init__ with common fields
        super().__init__(artist, album, duration_seconds)
        self.title = title

    def play_time_formatted(self):
        """Returns duration as MM:SS (zero-padded)."""
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def __str__(self):
        """Returns string format: (<artist>) <album>, duration: <MM:SS>"""
        return f"({self.artist}) {self.album}, duration: {self.play_time_formatted()}"

# --- Example Usage ---
#if __name__ == "__main__":
#song1 = Song("Kendrick Lamar", "DAMN.", 220, "Humble")
#song2 = Song("Kendrick Lamar", "DAMN.", 65, "DNA.")    
#print(song1)  # (Kendrick Lamar) DAMN., duration: 03:40
#print(song2)  # (Kendrick Lamar) DAMN., duration: 01:05
