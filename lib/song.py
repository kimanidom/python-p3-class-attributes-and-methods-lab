class Song:
    # Class attributes to track songs, artists, and genres
    count = 0
    artists = set()
    genres = set()
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.count += 1

        Song.artists.add(artist)
        Song.genres.add(genre)

        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
