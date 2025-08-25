# Given a number of bitcoins, display the current price
import sys

import requests

api_key = 'fb87dc6c7f4f60414ffe89875f74378628457aa63c0d41ec325ff2fbf8842600'


def main():
    try:
        value = sys.argv[1]

        bitcoins = float(value)
    except ValueError | IndexError:
        sys.exit('Please provide a single argument that can be converted to a floating point value')

    price = get_price()

    print(f'${price * bitcoins:,.4f}')


def get_price():
    url = f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}'

    try:
        response = requests.get(url)
    except requests.RequestException:
        print(requests.RequestException)
        return 0.0

    try:
        data = response.json()
        return float(data['data']['priceUsd'])
    except KeyError:
        print(f'"priceUsd" was not in response. response={response}')
        return 0.0
    except ValueError:
        print(f'Could not convert "priceUsd" to a float. response={response}')
        return 0.0


if __name__ == '__main__':
    main()
