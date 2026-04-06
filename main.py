"""
Driver script demonstrating the complete Music Track hierarchy.

Run:
    python main.py

Expected output
---------------
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False

After sorting:
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
"""

class Track:
    def __init__(self, artist, genre, album, title, active_years, duration, explicit=False):
        self.artist = artist
        self.genre = genre
        self.album = album
        self.title = title
        self.active_years = active_years
        self.duration = duration  # in seconds
        self.explicit = explicit

    def get_release_year(self):
        # Extract the first year from "YYYY–YYYY"
        return int(self.active_years.split('–')[0])

    def __repr__(self):
        return f"Track('{self.title}', '{self.artist}', {self.get_release_year()})"

class Playlist:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def sort_by_release_year(self):
        self.tracks.sort(key=lambda x: x.get_release_year())

    def __repr__(self):
        return "Playlist([\n    " + ",\n    ".join([str(t) for t in self.tracks]) + "\n])"

if __name__ == "__main__":
    # 1. Create tracks
    t1 = Track("Kendrick Lamar", "Hip-Hop", "DAMN.", "Song", "2017–2018", 220, explicit=True)
    t2 = Track("Alanis Morissette", "Alternative", "Jagged Little Pill", "Song", "1995–1996", 245, explicit=False)
    t3 = Track("Joe Rogan", "Comedy", "The Joe Rogan Experience", "Podcast", "2009–2010", 9000, explicit=True)
    t4 = Track("Sarah Koenig", "Journalism", "Serial", "Podcast", "2014–2015", 5400, explicit=False)

    # 2. Instantiate Playlist and add tracks
    p = Playlist()
    p.add_track(t1)
    p.add_track(t2)
    p.add_track(t3)
    p.add_track(t4)

    # 3. Print before sorting
    print("Before sorting:")
    print(p)

    # 4. Sort
    p.sort_by_release_year()

    # 5. Print after sorting
    print("\nAfter sorting:")
    print(p)