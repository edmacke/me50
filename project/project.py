import re

from tabulate import tabulate

import args
from client import SpotifyClient


def main(client: SpotifyClient = None):
    # Get arguments from command line
    user_args = args.get_args()

    # Get a handle to the Spotify API
    if not client:
        client = SpotifyClient()
        client.connect(client_id=user_args['id'], client_secret=user_args['secret'])

    # Get all tracks for all playlists
    tracks = get_all_tracks(client=client, user=user_args['user'])

    # Find duplicate tracks
    duplicate_tracks = find_duplicate_tracks(tracks)

    # Print duplicate tracks
    print_list(duplicate_tracks)


def normalize_name(name: str) -> str:
    # Convert name to lower case
    name = name.lower()

    # Remove any instances of remaster, e.g. "Title - 2013 Remaster" will return "title"
    return re.sub(r'( - \d\d\d\d remaster)$', '', name)


def get_all_tracks(client: SpotifyClient, user: str) -> list[dict]:
    tracks: list[dict] = list()

    # Get all playlists belonging to user
    playlists = client.get_playlists(user=user)

    # For each playlist found, get all tracks
    for playlist in playlists:
        tracks = client.get_tracks_for_playlist(playlist)

    # Compute keys for returned tracks
    for track in tracks:
        track['duplicate_key'] = f'{track['playlist'].lower()}-{track['artist'].lower()}-{normalize_name(track['name'])}'
        track['sort_key'] = f'{track['playlist'].lower()}-{track['artist'].lower()}-{track['name'].lower()}-{track['album'].lower()}'

    # Return list of all tracks for all playlists
    return tracks


def find_duplicate_tracks(tracks: list[dict]) -> list[dict]:
    track_counts: dict = dict()

    # For each track, either create or increment a counter based on track's "duplicate key" which
    # uniquely identifies track for purposes of duplicate checking
    for track in tracks:
        key = track['duplicate_key']
        if key in track_counts:
            track_counts[key] += 1
        else:
            track_counts[key] = 1

    # Create new dictionary having only tracks with > 1 instances
    track_counts = {key: value for key, value in track_counts.items() if value > 1}

    # Return list of items whose keys are in the dictionary of tracks with > 1 instances
    return [t for t in tracks if t['duplicate_key'] in track_counts.keys()]


def create_print_tracks(tracks: list[dict]) -> list[dict]:
    print_tracks: list[dict] = list()

    for track in tracks:
        item = dict()
        item['Playlist'] = track['playlist']
        item['Artist'] = track['artist']
        item['Title'] = track['name']
        item['Album'] = track['album']
        print_tracks.append(item)

    return print_tracks


def print_list(tracks: list[dict]):
    sorted_tracks = sorted(tracks, key=lambda x: x['sort_key'])

    print_tracks = create_print_tracks(sorted_tracks)

    print(tabulate(print_tracks, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()
