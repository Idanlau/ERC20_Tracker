from erc20_tokens import get_erc20_tokens
from token_info import get_num_holders
from more_than_10k import more_than_10k

get_erc20_tokens() # Get of erc20 tokens lists, outputs in active_tokens_list.csv
get_num_holders() # Gets number of holders for the token, outputs in num_holders_tokens_list.csv
more_than_10k() # Gets tokens with more than 10k holders, outputs in contracts_with_more_than_10k_holders.csv


