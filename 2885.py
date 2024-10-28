import pandas as pd

def rename_columns(df):
    df = df.rename(columns = {'id':'student_id', 'first':'first_name', 'last':'last_name', 'age':'age_in_years'})
    return df