from spotipy import Spotify

from api import API


class SpotifyMock(Spotify):
    def user_playlists(self, user: str, **kwargs):
        response = {}
        response['items'] = [
            {'name': 'Playlist1', 'id': '1', 'owner': {'id': 'owner_id'}},
            {'name': 'Playlist2', 'id': '2', 'owner': {'id': 'owner_id'}},
            {'name': 'Playlist3', 'id': '3', 'owner': {'id': 'somebody_else'}}
        ]

        return response

    def playlist_items(self, **kwargs):
        items = list()
        for i in range(40):
            item = dict()
            item['track'] = {}
            item['track']['name'] = f'track_{i}_name'
            item['track']['album'] = {'name': f'track_name_{i}_album_name'}
            item['track']['uri'] = f'track_{i}_uri'
            item['track']['id'] = f'track_{i}_id'
            item['track']['disc_number'] = f'track_{i}_disc_number'
            item['track']['track_number'] = f'track_{i}_track_number'
            item['track']['artists'] = [f'track_{i}_artist_name']
            items.append(item)

        return items


def test_get_playlists():
    obj = API(client_id='', client_secret='', username='owner_id')
    obj.api = SpotifyMock()
    playlists = obj.get_playlists()

    assert 2 == len(playlists)
    assert 'Playlist1' == playlists[0]['name']
    assert 'Playlist2' == playlists[1]['name']

def test_get_tracks():
    obj = API(client_id='', client_secret='', username='owner_id')
    obj.api = SpotifyMock()
    playlists = obj.get_playlists()

    for playlist in playlists:
        tracks = obj.get_tracks_for_playlist(playlist)
