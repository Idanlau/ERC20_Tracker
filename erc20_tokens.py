from requests import Session
import json
import pprint
import pandas as pd
from dotenv import load_dotenv
import os


def get_erc20_tokens():
    
    load_dotenv()
    COIN_MARKET_CAP_API_KEY = os.getenv('COIN_MARKET_CAP_API_KEY')

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COIN_MARKET_CAP_API_KEY
    } 

    parameters = {}

    session = Session() # Create new session object to manage API requests
    session.headers.update(headers) #Update the session headers with the specified headers

    response = session.get(url, params=parameters) # Receiving the response from the API

    info = json.loads(response.text)
    tokens = info['data'] # Filter to get only the token data

    data = {
    'Name': [],
    'Token Address': []
    }

    for token in info['data']:
        if token.get('platform'): # Make sure the token has an attribute of platform
            if token['platform'].get('symbol') == 'ETH': # Filter for tokens built on erc20
                data['Name'].append(token['name'])
                data['Token Address'].append(token['platform']['token_address'])

    df = pd.DataFrame(data)
    print(df.head())

    df.to_csv('active_tokens_list.csv')

    print("Token count:", len(df))

