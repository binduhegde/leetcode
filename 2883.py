import pandas as pd

def drop_missing(df):
    df.dropna(subsets = ['name'], inplace=True)
    return df