from client import SpotifyClient
from test_helper import SpotifyMock


def generate_playlists(count: int, username: str) -> list[dict]:
    items: list[dict] = list()

    for i in range(count - 1):
        item = {'name': f'Playlist{i}', 'id': str(i), 'owner': {'id': username}}
        items.append(item)

    item = {'name': 'Playlist999', 'id': '999', 'owner': {'id': 'somebody_else'}}
    items.append(item)

    return items


def generate_tracks(count: int) -> list[dict]:
    items: list[dict] = list()

    for i in range(count):
        item = dict()
        item['track'] = {}
        item['track']['name'] = f'track_{i}_name'
        item['track']['album'] = {'name': f'track_{i}_album_name'}
        item['track']['id'] = f'track_{i}_id'
        item['track']['artists'] = [{'name': f'track_{i}_artist_name'}]
        item['track']['type'] = 'track'
        items.append(item)

    return items


def test_get_playlists():
    obj = SpotifyClient()
    obj.api = SpotifyMock()
    obj.api.playlists = generate_playlists(110, 'owner_id')
    playlists = obj.get_playlists(user='owner_id')

    assert 109 == len(playlists) # 110 playlists, but 1 doesn't belong to user
    assert 'Playlist0' == playlists[0]['name']
    assert 'Playlist1' == playlists[1]['name']


def test_get_tracks():
    obj = SpotifyClient()
    obj.api = SpotifyMock()
    obj.api.playlists = generate_playlists(110, 'owner_id')
    obj.api.tracks = generate_tracks(203)
    playlists = obj.get_playlists(user='owner_id')

    playlist = playlists[0]

    tracks = obj.get_tracks_for_playlist(playlist)

    assert 203 == len(tracks)

    assert playlist['name'] == tracks[0]['playlist']
    assert 'track_0_name' == tracks[0]['name']


def test_episode():
    obj = SpotifyClient()
    obj.api = SpotifyMock()
    obj.api.playlists = generate_playlists(3, 'owner_id')
    obj.api.tracks = generate_tracks(20)
    playlists = obj.get_playlists(user='owner_id')

    episode = dict()
    episode['track'] = {}
    episode['track']['name'] = f'track_bad_name'
    episode['track']['type'] = 'episode'

    obj.api.tracks.append(episode)

    tracks = obj.get_tracks_for_playlist(playlists[0])
    assert 20 == len(tracks)
