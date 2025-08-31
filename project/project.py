from tabulate import tabulate

import api
import args
import test_api
from api import Track


def main():
    duplicate_tracks: list[Track] = list()

    # Get arguments from command line
    user_args = args.get_args()

    # Create instance of Spotify API object and perform authorization
    spotify_api = api.API(client_id=user_args['id'], client_secret=user_args['secret'], username=user_args['user'])
    spotify_api.api = test_api.SpotifyMock(user_args['user'])
    # spotify_api.connect()

    # Get all playlists belonging to user
    playlists = spotify_api.get_playlists()

    # For each playlist, find duplicate tracks
    for playlist in playlists:
        tracks = spotify_api.get_tracks_for_playlist(playlist)

        duplicate_tracks.extend([track for track in tracks if tracks.count(track) > 1])
        duplicate_tracks.extend(tracks)

    print_list(tracks)


def print_list(tracks: list[Track]):
    headers = {'playlist_name'}

    sorted_list = sorted(tracks, key=lambda item: item.sort_key)

    sorted_dict = [vars(item) for item in sorted_list]

    print(tabulate(sorted_dict, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()
