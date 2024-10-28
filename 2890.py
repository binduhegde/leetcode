import pandas as pd

def melt_df(df):
    # Use the 'melt' function to reshape the DataFrame.
    # The 'id_vars' parameter specifies the columns to be retained as identifier variables ('product' in this case).
    # The 'var_name' parameter specifies the name for the variable column ('quarter' in this case).
    # The 'value_name' parameter specifies the name for the value column ('sales' in this case).
    new_df = pd.melt(df, id_vars= ['product'], var_name= 'quarter', value_name='sales')