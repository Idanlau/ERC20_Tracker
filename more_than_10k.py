import pandas as pd


def more_than_10k():
    
    file_path = 'num_holders_tokens_list.csv'
    df = pd.read_csv(file_path)

    df['Num Holders'] = pd.to_numeric(df['Num Holders'], errors='coerce')
    df_filtered = df[df['Num Holders'] >= 10000]

    df_filtered = df_filtered[["Name","Token Address","Num Holders"]] # Save the Name, Token Address and Num Holders
    df_filtered.to_csv('contracts_with_more_than_10k_holders.csv', index=False)