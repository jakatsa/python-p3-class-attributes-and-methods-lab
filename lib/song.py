class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    all_songs = []

#functions
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        Song.all_songs.append(self)
        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        for genre in cls.genres:
            cls.genre_count[genre] = sum(1 for song in cls.all_songs if song.genre == genre)

    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artists:
            cls.artist_count[artist] = sum(1 for song in cls.all_songs if song.artist == artist)
