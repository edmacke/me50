import uuid
from typing import Self

from spotipy import CacheFileHandler, Spotify
from spotipy.oauth2 import SpotifyOAuth


class Track:
    def __init__(self):
        self.playlist_name: str = ''
        self.playlist_id: str = ''
        self.track_name: str = ''
        self.artist: str = ''
        self.album_name: str = ''
        self.uri: str = ''
        self.track_id: str = ''
        self.disc_number: int = 0
        self.track_number: int = 0
        self.guid: str = str(uuid.uuid4())

    @property
    def sort_key(self) -> str:
        return f'{self.playlist_name}-{self.artist}-{self.track_name}-{self.album_name}-{self.disc_number:03d}-{self.track_number:03d}'.lower()

    @property
    def duplicate_sort_key(self) -> str:
        return f'{self.playlist_name}-{self.artist}-{self.track_name}-{self.album_name}-{self.disc_number:03d}-{self.track_number:03d}'.lower()

    @property
    def compare_key(self) -> str:
        return f'{self.playlist_name.lower()}-{self.artist.lower()}-{self.track_name.lower()}'.lower()

    def __eq__(self, other: Self):
        return self.compare_key == other.compare_key


class API:
    def __init__(self, client_id: str, client_secret: str, username: str):
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.username: str = username
        self.api: Spotify | None = None

    def connect(self):
        cache_handler = CacheFileHandler(cache_path='.spotify_cache')

        auth_manager = SpotifyOAuth(cache_handler=cache_handler,
                                    scope='playlist-read-private',
                                    client_id=self.client_id,
                                    client_secret=self.client_secret,
                                    redirect_uri='http://127.0.0.1:9090')

        self.api = Spotify(auth_manager=auth_manager)

    def get_playlists(self) -> list[dict]:
        # Get all playlists for user
        response = self.api.user_playlists(user=self.username, limit=50)

        if len(response['items']) >= 50:
            print('This app only supports a maximum of 50 personal playlists. Only the first 50 will be analyzed')

        # Filter out playlists not owner by user (e.g. other people's playlists added by user)
        playlists = [playlist for playlist in response['items'] if playlist['owner']['id'] == self.username]

        return playlists

    def get_tracks_for_playlist(self, playlist: dict) -> list[Track]:
        tracks: list[Track] = list()

        playlist_name = playlist['name']
        playlist_id = playlist['id']

        count = playlist['tracks']['total']
        offset = 0

        while True:
            # Get tracks for passed playlist
            response = self.api.playlist_items(playlist_id=playlist_id, offset=offset, limit=5)
            items = response['items']

            for item in items:
                track = Track()
                track.playlist_name = playlist_name
                track.playlist_id = playlist_id
                track.track_name = item['track']['name']
                track.album_name = item['track']['album']['name']
                track.uri = item['track']['uri']
                track.track_id = item['track']['id']
                track.disc_number = item['track']['disc_number']
                track.track_number = item['track']['track_number']
                artists = item['track']['artists']
                if len(artists) > 0:
                    track.artist = artists[0]['name']

                tracks.append(track)

            if len(items) == 0:
                break
            else:
                offset = offset + len(items)

        return tracks
