from random import sample

class Playlist():
    def __init__(self):
        self._songs = []

    def songs(self):
        print(self._songs)

    def add_song(self, song_name, song_length, artist):
        self._songs.append({ 
            "name": song_name, 
            "length": song_length, 
            "artist": artist 
        })

    def shuffle(self):
        return sample(self._songs, len(self._songs))
    
playlist = Playlist()
playlist.songs()
playlist.add_song("Baby Shark", "infinite", "a demon")
playlist.add_song("Pink Pony Club", "a longer infinite", "a more torturous demon")
playlist.add_song("Crab Rave", "???", "The crabs, presumably")
playlist.songs()

print(playlist.shuffle())