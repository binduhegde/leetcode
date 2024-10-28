import pandas as pd

def fill(df):
    df['quantity'] = df['quantity'].fillna(0)
    return df