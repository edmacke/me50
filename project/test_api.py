from spotipy import Spotify

from api import API


class SpotifyMock(Spotify):
    def __init__(self, username: str):
        super().__init__()
        self.called: bool = False
        self.username = username

    def user_playlists(self, user, limit=50, offset=0, **kwargs) -> dict:
        if self.called:
            self.called = False
            return {"items": []}

        response = dict()
        response['items'] = [
            {'name': 'Playlist1', 'id': '1', 'owner': {'id': self.username}},
            {'name': 'Playlist2', 'id': '2', 'owner': {'id': self.username}},
            {'name': 'Playlist3', 'id': '3', 'owner': {'id': 'somebody_else'}}
        ]

        self.called = True

        return response

    def playlist_items(self, playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=None, **kwargs):
        if self.called:
            self.called = False
            return {"items": []}

        items = list()
        for i in range(40):
            item = dict()
            item['track'] = {}
            item['track']['name'] = f'track_{i}_name'
            item['track']['album'] = {'name': f'track_name_{i}_album_name'}
            item['track']['uri'] = f'track_{i}_uri'
            item['track']['id'] = f'track_{i}_id'
            item['track']['disc_number'] = 1
            item['track']['track_number'] = 1
            item['track']['artists'] = [{'name': f'track_{i}_artist_name'}]
            items.append(item)

        response = dict()
        response['items'] = items

        self.called = True

        return response


def test_get_playlists():
    obj = API(client_id='', client_secret='', username='owner_id')
    obj.api = SpotifyMock('owner_id')
    playlists = obj.get_playlists()

    assert 2 == len(playlists)
    assert 'Playlist1' == playlists[0]['name']
    assert 'Playlist2' == playlists[1]['name']


def test_get_tracks():
    obj = API(client_id='', client_secret='', username='owner_id')
    obj.api = SpotifyMock('owner_id')
    playlists = obj.get_playlists()

    for playlist in playlists:
        tracks = obj.get_tracks_for_playlist(playlist)

        assert playlist['name'] == tracks[0].playlist_name
        assert 'track_0_name' == tracks[0].name
