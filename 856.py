import pandas as pd

def find_customer(df):
    highest_count = df['customer_number'].value_counts()#.max()
    return highest_count
    new_data = df[df['customer_number'] == highest_count]['customer_number'].to_list()
    new_df = pd.DataFrame(data={'customer_number':new_data})
    return new_df



dicti = {'order_number':[1,2,3,4], 'customer_number':[1,2,3,3]}
df = pd.DataFrame(data=dicti)
print(find_customer(df))