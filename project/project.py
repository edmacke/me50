import re

from tabulate import tabulate

import args
from client import SpotifyClient


def main(client: SpotifyClient = None):
    # Get arguments from command line
    user_args = args.get_args()

    # If not passed a client object (test only), create client and authenticate using creds passed on command line
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
    name = re.sub(r'( - \d\d\d\d remaster)$', '', name)

    name = re.sub(r'( - remastered \d\d\d\d$)$', '', name)

    return name


def get_all_tracks(client: SpotifyClient, user: str) -> list[dict]:
    tracks: list[dict] = list()

    # Get all playlists belonging to user
    playlists = client.get_playlists(user=user)

    # For each playlist found, get all tracks and append to list to be returned
    for playlist in playlists:
        playlist_tracks = client.get_tracks_for_playlist(playlist)
        tracks.extend(playlist_tracks)

    tracks = add_track_keys(tracks)

    return tracks


def add_track_keys(tracks: list[dict]) -> list[dict]:
    # Compute keys for all returned tracks
    # duplicate_key is a value used to determine if a track is the same as another (i.e. equals)
    # sort_key is a value used to sort final output
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

    # Filter out tracks only having 1 instance. Remaining items are all duplicate tracks
    track_counts = {key: value for key, value in track_counts.items() if value > 1}

    # Return list of items whose keys are in the dictionary of tracks with > 1 instances
    return [t for t in tracks if t['duplicate_key'] in track_counts.keys()]


def create_print_tracks(tracks: list[dict]) -> list[dict]:
    print_tracks: list[dict] = list()

    # For each track, simply create a new dictionary that's print-friendly and doesn't include working items like sort_keys
    for track in tracks:
        item = dict()
        item['Playlist'] = track['playlist']
        item['Artist'] = track['artist']
        item['Title'] = track['name']
        item['Album'] = track['album']
        print_tracks.append(item)

    return print_tracks


def print_list(tracks: list[dict]):
    # Sort list of tracks according to its sort_key (Playlist, Artist, Title, Album)
    sorted_tracks = sorted(tracks, key=lambda x: x['sort_key'])

    # Create print-friendly version of tracks
    print_tracks = create_print_tracks(sorted_tracks)

    # Print table with duplicate tracks
    print(tabulate(print_tracks, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()
