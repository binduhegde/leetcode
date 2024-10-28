import pandas as pd

def get_size(df):
    num_rows, num_columns = df.shape
    return num_rows, num_columns

# creating a random df. has 10 rows and 4 columns
data = [[j for i in range(4)] for j in range(10)]
df = pd.DataFrame(data, columns= ['name', 'num', 'money', 'yes'])

print(get_size(df))