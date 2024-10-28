import pandas as pd

def convert_type(df):
    df['grade'] = df['grade'].astype(int)
    return df