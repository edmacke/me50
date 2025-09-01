from spotipy import CacheFileHandler, Spotify
from spotipy.oauth2 import SpotifyOAuth


class SpotifyClient:
    def __init__(self):
        self.api: Spotify | None = None

    def connect(self, client_id: str, client_secret: str):
        cache_handler = CacheFileHandler(cache_path='.spotify_cache')

        auth_manager = SpotifyOAuth(cache_handler=cache_handler,
                                    scope='playlist-read-private',
                                    client_id=client_id,
                                    client_secret=client_secret,
                                    redirect_uri='http://127.0.0.1:9090')

        self.api = Spotify(auth_manager=auth_manager)

    def get_playlists(self, user: str) -> list[dict]:
        playlists: list[dict] = list()
        offset = 0

        while True:
            # Get all playlists for user. See https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists
            response = self.api.user_playlists(user=user, offset=offset)

            items = response['items']
            if len(items) == 0:
                break

            # Filter out playlists not owner by user (e.g. other people's playlists added by user)
            playlists.extend([playlist for playlist in items if playlist['owner']['id'] == user])

            offset += len(items)

        return playlists

    def get_tracks_for_playlist(self, playlist: dict) -> list[dict]:
        tracks: list[dict] = list()

        playlist_name = playlist['name']
        playlist_id = playlist['id']

        offset = 0

        while True:
            # Get tracks for passed playlist. See https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
            response = self.api.playlist_items(playlist_id=playlist_id, offset=offset, limit=50)
            items = response['items']

            if len(items) == 0:
                break

            for item in items:
                if item['track']['type'] == 'track':
                    track = dict()
                    track['playlist'] = playlist_name
                    track['name'] = item['track']['name']
                    track['album'] = item['track']['album']['name']

                    artists = item['track']['artists']
                    if len(artists) > 0:
                        track['artist'] = artists[0]['name']

                    tracks.append(track)

            offset = offset + len(items)

        return tracks
