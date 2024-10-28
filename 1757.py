import pandas as pd

def find_products(df):
    new_df = df[(df['low_fats'] == 'Y') & (df['recyclable'] == 'Y')]
    return new_df[['product_id']]


data = [[0, 'Y', 'N'], [1, 'Y', 'Y'], [2, 'N', 'Y'], [3, 'Y', 'Y'], [4, 'N', 'N']]
df = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable'])

print(find_products(df))