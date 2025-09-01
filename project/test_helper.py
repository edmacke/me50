from spotipy import Spotify


# Class to mock API calls to Spotify API
class SpotifyMock(Spotify):
    def __init__(self):
        super().__init__()
        self.playlists: list[dict] = list()
        self.playlist_offset = 0
        self.tracks: list[dict] = list()
        self.track_offset: int = 0

    # Override API function to return list of 99 playlists
    def user_playlists(self, user, limit=50, offset=0, **kwargs) -> dict:
        response = {'items': list()}

        if self.playlist_offset > len(self.playlists):
            return response

        response['items'] = self.playlists[self.playlist_offset:self.playlist_offset + 50]
        self.playlist_offset += 50

        return response

    # Override API function to return list of 110 playlists
    def playlist_items(self, playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=None, **kwargs):
        response = {'items': list()}

        if self.track_offset > len(self.tracks):
            return response

        response['items'] = self.tracks[self.track_offset:self.track_offset + 50]
        self.track_offset += 50

        return response
