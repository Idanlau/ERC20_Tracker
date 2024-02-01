# ERC20 tokens: no. of holders tracker
This script pulls active tokens from the CoinMarketCap API and gets the no. of holders information from the Ethplorer API. The final results are stored in contracts_with_more_than_10k_holders.csv where it shows erc20 tokens with more than 10k holders.

## File Structure

```bash
.env # Stores the API keys

worker.py # Orchestrator file

erc20_tokens.py # Pulls active tokens from coin market cap API

token_info.py # Pulls no. of holders based on contract address from Ethplorer API

more_than_10k.py # Filters for tokens with > 10k holders

num_holders_tokens_list.csv # Result file
```

## Running it

```bash
pip3 install -r requirements.txt
```

```bash
python3 worker.py
```



