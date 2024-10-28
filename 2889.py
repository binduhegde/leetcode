import pandas as pd

def pivot_table(df):
    return df.pivot_table(index='month', columns='city', values='temperature')