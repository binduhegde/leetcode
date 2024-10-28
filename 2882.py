import pandas as pd

def drop_duplicates(df):
    return df.drop_duplicates(subset = ['email'])