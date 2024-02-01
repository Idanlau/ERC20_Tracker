import requests
import json
import pprint
import pandas as pd
from dotenv import load_dotenv
import os

def get_num_holders():

    load_dotenv()
    ETHPLORER_API_KEY = os.getenv('ETHPLORER_API_KEY')


    file_path = 'active_tokens_list.csv'
    df = pd.read_csv(file_path)
    
    df['Num Holders'] = None

    for index, row in df.iterrows():
        token_addr = row['Token Address']
        url = f'https://api.ethplorer.io/getTokenInfo/{token_addr}?apiKey={ETHPLORER_API_KEY}' # url format
        response = requests.get(url)  # Making the API call
        info = json.loads(response.text) # Data from response
        
        if 'holdersCount' in info: # If holdersCount is avaliable
            df.at[index, 'Num Holders'] = info['holdersCount']
            print(token_addr, info['holdersCount'])
        else:
            df.at[index, 'Num Holders'] = None

    df.to_csv('num_holders_tokens_list.csv',index=False)


    