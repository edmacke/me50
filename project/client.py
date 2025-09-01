from spotipy import CacheFileHandler, Spotify
from spotipy.oauth2 import SpotifyOAuth


# Class to handle authentication to Spotify API, make paged API calls, and return app-friendly dictionaries
class SpotifyClient:
    def __init__(self):
        self.api: Spotify | None = None

    # Using passed credentials, create an API object and authenticate
    def connect(self, client_id: str, client_secret: str):
        cache_handler = CacheFileHandler(cache_path='.spotify_cache')

        # Client ID and Secret must be created at https://developer.spotify.com/dashboard
        auth_manager = SpotifyOAuth(cache_handler=cache_handler,
                                    scope='playlist-read-private',
                                    client_id=client_id,
                                    client_secret=client_secret,
                                    redirect_uri='http://127.0.0.1:9090')

        self.api = Spotify(auth_manager=auth_manager)

    # Get all playlists for which the passed user is the owner
    def get_playlists(self, user: str) -> list[dict]:
        playlists: list[dict] = list()
        offset = 0

        while True:
            # Get all playlists for user. See https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists
            response = self.api.user_playlists(user=user, offset=offset)

            # Get list of items returned by Spotify. If 0, no more playlists so we can break out of loop
            items = response['items']
            if len(items) == 0:
                break

            # Filter out playlists not owner by user (e.g. other people's playlists added by user)
            playlists.extend([playlist for playlist in items if playlist['owner']['id'] == user])

            # Compute offset as the previous offset plus the count of items returned by this call
            offset += len(items)

        return playlists

    # Get all tracks for the passed playlist. Ignores any 'episode' entries returned by Spotify
    def get_tracks_for_playlist(self, playlist: dict) -> list[dict]:
        tracks: list[dict] = list()

        playlist_name = playlist['name']
        playlist_id = playlist['id']

        offset = 0

        while True:
            # Get tracks for passed playlist. See https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
            response = self.api.playlist_items(playlist_id=playlist_id, offset=offset, limit=50)
            items = response['items']

            # Get list of items returned by Spotify. If 0, no more playlists so we can break out of loop
            if len(items) == 0:
                break

            # For each track returned, create new dictionary object and append to list to be returned
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

            # Compute offset as the previous offset plus the count of items returned by this call
            offset = offset + len(items)

        return tracks
