import argparse


def get_args() -> dict:
    # Create argument parser object
    parser = argparse.ArgumentParser(description='Spotify Duplication Detector', epilog='Client ID and Secret should be set up at https://developer.spotify.com/dashboard/applications. Username is from your Spotify profile.')

    # Add expected arguments - all 3 are required
    parser.add_argument('-i', '--id', type=str, help='client id from Spotify developer page', required=True)
    parser.add_argument('-s', '--secret', type=str, help='client secret from Spotify developer page', required=True)
    parser.add_argument('-u', '--user', type=str, help='Spotify username', required=True)

    # Return dictionary of arguments
    return vars(parser.parse_args())
