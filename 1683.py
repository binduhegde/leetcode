import pandas as pd

def invalid_tweets(df):
    new_df = df[df['content'].str.len() > 15][['tweet_id']]
    return new_df