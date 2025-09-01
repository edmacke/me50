import sys

import project
from client import SpotifyClient
from test_helper import SpotifyMock

# List of dctionary objects representing individual tracks as Spotify would return them
test_tracks = [
    {'track': {
        'type': 'track', 'name': 'American Girl', 'album': {'name': 'American Girl'}, 'id': '1', 'artists': [{'name': 'Dierks Bently'}]
    }},
    {'track': {
        'type': 'track', 'name': 'American Girl', 'album': {'name': 'Tom Petty & The Heartbreakers'}, 'id': '2', 'artists': [{'name': 'Tom Petty & The Heartbreakers'}]
    }},
    {'track': {
        'type': 'track', 'name': 'And She Was', 'album': {'name': 'Little Creatures'}, 'id': '3', 'artists': [{'name': 'Talking Heads'}]
    }},
    {'track': {
        'type': 'track', 'name': 'And She Was - 2003 Remaster', 'album': {'name': 'Once in a Lifetime: The Talking Heads Box (2003 Remaster)'}, 'id': '4', 'artists': [{'name': 'Talking Heads'}]
    }},
    {'track': {
        'type': 'track', 'name': 'Eat It', 'album': {'name': 'Weird: The Weird Al Yankovic Story'}, 'id': '5', 'artists': [{'name': '"Weird Al" Yankovic'}]
    }},
    {'track': {
        'type': 'track', 'name': 'Eat It', 'album': {'name': 'The Essential "Weird Al" Yankovic'}, 'id': '6', 'artists': [{'name': '"Weird Al" Yankovic'}]
    }},
    {'track': {
        'type': 'track', 'name': 'Eat It', 'album': {'name': 'In 3-D'}, 'id': '7', 'artists': [{'name': '"Weird Al" Yankovic'}]
    }}
]


# Construct a client and mock API that will return a playlist='Duplicates' with test tracks above
def get_test_tracks():
    client = SpotifyClient()

    client.api = SpotifyMock()

    client.api.playlists = [{'name': 'Duplicates', 'id': '1', 'owner': {'id': 'username'}}, {'name': 'Playlist2', 'id': '2', 'owner': {'id': 'username'}}]
    client.api.tracks = test_tracks

    return project.get_all_tracks(client=client, user='username')


# Make sure client returns properly formatted track list
def test_get_tracks():
    tracks = get_test_tracks()
    assert 7 == len(tracks)

    assert 'duplicates-dierks bently-american girl' == tracks[0]['duplicate_key']
    assert 'duplicates-dierks bently-american girl-american girl' == tracks[0]['sort_key']


# Make sure name is lower case and remaster isn't counted
def test_normalize_name():
    assert 'and she was' == project.normalize_name('And She Was')
    assert 'and she was' == project.normalize_name('And She Was - 2003 Remaster')
    assert 'and she was' == project.normalize_name('And She Was - Remastered 2011')


# Test finding duplicates
def test_find_duplicates():
    tracks = get_test_tracks()

    duplicate_tracks = project.find_duplicate_tracks(tracks)

    keys = [t['duplicate_key'] for t in duplicate_tracks]

    assert 'duplicates-"weird al" yankovic-eat it' in keys
    assert 'duplicates-talking heads-and she was' in keys
    assert not 'duplicates-dierks bently-american girl' in keys


# Test conversion of tracks to print-friendly tracks
def test_create_print_tracks():
    tracks = get_test_tracks()

    tracks = project.create_print_tracks(tracks)

    assert 'Duplicates' == tracks[6]['Playlist']
    assert '"Weird Al" Yankovic' == tracks[6]['Artist']
    assert 'Eat It' == tracks[6]['Title']
    assert 'In 3-D' == tracks[6]['Album']


def test_print():
    tracks = get_test_tracks()

    duplicate_tracks = project.find_duplicate_tracks(tracks)

    project.print_list(duplicate_tracks)


def test_main():
    sys.argv = ['test_args', '-i', 'id', '-s', 'secret', '-u', 'userid']

    client = SpotifyClient()

    client.api = SpotifyMock()

    client.api.playlists = [{'name': 'Duplicates', 'id': '1', 'owner': {'id': 'username'}}]
    client.api.tracks = test_tracks

    project.main(client=client)


def test_readme():
    tracks = [
        {'playlist': 'My Songs', 'name': 'And She Was', 'album': 'Little Creatures', 'artist': 'Talking Heads'},
        {'playlist': 'My Songs', 'name': 'And She Was - 2003 Remaster', 'album': 'Once in a Lifetime: The Talking Heads Box (2003 Remaster)', 'artist': 'Talking Heads'},
        {'playlist': 'My Songs', 'name': 'Animal', 'album': 'Habits', 'artist': 'Neon Trees'},
        {'playlist': 'My Songs', 'name': 'Animal', 'album': 'Hysteria', 'artist': 'Def Leppard'},
        {'playlist': 'My Songs', 'name': 'Eat It', 'album': 'Weird: The Weird Al Yankovic Story', 'artist': '"Weird Al" Yankovic'},
        {'playlist': 'My Songs', 'name': 'Eat It', 'album': 'The Essential "Weird Al" Yankovic', 'artist': '"Weird Al" Yankovic'},
        {'playlist': 'My Songs', 'name': 'Eat It', 'album': 'In 3-D', 'artist': '"Weird Al" Yankovic'},
        {'playlist': 'My Songs', 'name': 'Bohemian Rhaposdy - Live Aid', 'album': 'Bohemian Rhaposdy (The Original Soundtrack)', 'artist': 'Queen'},
        {'playlist': 'My Songs', 'name': 'Bohemian Rhaposdy - Remastered 2011', 'album': 'A Night At The Opera', 'artist': 'Queen'},
        {'playlist': 'My Songs', 'name': 'Bohemian Rhaposdy', 'album': 'The Best Songs Of All Time', 'artist': 'Queen'},
        {'playlist': 'Polka', 'name': 'Eat It', 'album': 'In 3-D', 'artist': '"Weird Al" Yankovic'}
    ]

    tracks = project.add_track_keys(tracks)

    duplicate_tracks = project.find_duplicate_tracks(tracks)

    project.print_list(duplicate_tracks)
