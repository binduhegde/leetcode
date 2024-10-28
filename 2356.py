import pandas as pd

def unique_subjects(df):
    # naive method
    # teachers = set(df['teacher_id'].to_list())
    # result = {'teacher_id':[], 'cnt':[]}
    # for teacher in teachers:
    #     count = len(df[df['teacher_id'] == teacher]['subject_id'].unique())
    #     result['teacher_id'].append(teacher)
    #     result['cnt'].append(count)
    # return pd.DataFrame(data=result)

    # groupby method
    df = df.groupby(['teacher_id'])["subject_id"].nunique().reset_index()
    df = df.rename({'subject_id':'cnt'}, axis = 1)
    return df



table = {'teacher_id':[1,1,1,2,2,2,2],
         'subject_id':[2,2,3,1,2,3,4],
         'dept_id': [3,4,3,1,1,1,1]}
df = pd.DataFrame(data=table)
print(unique_subjects(df))

"""
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
Output:  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+"""