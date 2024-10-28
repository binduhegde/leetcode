import pandas as pd

def find_customers(customers, orders):
    df = customers[~customers['id'].isin(orders['customerId'])]
    new_df = df[['name']].rename(columns={'name':'customers'})
    return new_df


# creating customers df
customers_data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(customers_data, columns=['id', 'name'])

# creating order df
order_data = [[1,3],[2,1]]
orders = pd.DataFrame(order_data, columns= ['id', 'customerId'])

print(find_customers(customers, orders))