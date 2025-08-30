import args
import api


def main():
    user_args = args.get_args()

    spotify_api = api.API(client_id=user_args['id'], client_secret=user_args['secret'], username=user_args['user'])
    spotify_api.connect()

    playlists = spotify_api.get_playlists()

    for playlist in playlists:
        tracks = spotify_api.get_tracks_for_playlist(playlist)

    print(playlists)


if __name__ == '__main__':
    main()
