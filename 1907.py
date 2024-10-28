import pandas as pd 

# low less than 20000
# avg: 20-50k
# high: strictly > 50k
def count_salary(df):
    low = len(df[df['income'] < 20000])
    avg = len(df[(df['income'] <= 50000) & (df['income'] >= 20000)])
    high = len(df[df['income'] > 50000])
    result = {'category':['Low Salary', 'Average Salary', 'High Salary'],
              'accounts_count':[low, avg, high]}
    return pd.DataFrame(data=result)





data_list = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
df = pd.DataFrame(data= data_list, columns= ['account_id', 'income'])
print(count_salary(df))