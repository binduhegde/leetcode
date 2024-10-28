def rearrange_products(df):
    return df.melt(df, id_vars='product_id', vars_name='store', value_name='price').dropna()