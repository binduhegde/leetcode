import pandas as pd
def order_scores(df):
    # soring the df by scores in non ascending order
    df.sort_values(by='score', ascending=False, inplace=True)
    # getting a new column ranks and assigning it ranks
    df['rank'] = df['score'].rank(method='dense', ascending=False)
    # dropping the labels column
    df.drop(labels='id', axis= 1,inplace=True)
    return df
    



scores = {'id':[i for i in range(1, 7)], 'score':[3.5, 3.65, 4.0, 3.85, 4.0, 3.65]}
df = pd.DataFrame(data=scores)
print(order_scores(df))

"""
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
"""