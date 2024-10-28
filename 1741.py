import pandas as pd

def total_time(df):
    df['total_time'] = df['out_time'] - df['in_time']
    new_df = df[['event_day', 'emp_id', 'total_time']]
    new_df.columns= ['day', 'emp_id', 'total_time']
    return new_df.groupby(['day', 'emp_id']).sum().reset_index()

    # result = {'day':[], 'emp_id':[], 'total_time':[]}
    # id_set = set(df['emp_id'].to_list())
    # for employer in id_set:
    #     print("emloyer id:",employer)
    #     date_set = set(df[df['emp_id']==employer]['event_day'].to_list())
    #     for date in date_set:
    #         in_time = df[(df['event_day'] == date) & (df['emp_id'] == employer)]['in_time'].sum()
    #         out_time = df[(df['event_day'] == date) & (df['emp_id'] == employer)]['out_time'].sum()
    #         result['day'].append(date)
    #         result['emp_id'].append(employer)
    #         result['total_time'].append(out_time-in_time)

    # return pd.DataFrame(data = result)



data_dict = {'emp_id':[1,1,1,2,2], 
             'event_day':['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
             'in_time':[4,55,1,3,47], 
             'out_time':[32,200,42,33,74]}

df = pd.DataFrame(data=data_dict)
print(total_time(df))

"""
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
"""
"""Output: 
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+
"""