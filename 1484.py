import pandas as pd

def categorize_products(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()
    grouped.columns= ['sell_date', 'num_sold', 'products']
    grouped.sort_values(by='sell_date', inplace=True)
    return grouped


d = {'sell_date':["2020-06-01", "2020-06-02", "2020-05-30", "2020-06-01", "2020-06-02", "2020-05-30", "2020-05-30"],
        'product':["Pencil", "Mask", "Basketball", "Bible", "Mask", "T-Shirt", "Headphone"]
        }
df = pd.DataFrame(data=d)
print(categorize_products(df))




"""
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+
Output: 
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
"""