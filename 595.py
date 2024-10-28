def find_countries(df):
    new_df = df[(df['area'] >= 3000000) | (df['poulation'] >= 25000000)]
    return new_df[['name', 'population', 'area']]