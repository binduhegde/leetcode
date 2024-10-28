import pandas as pd

def find_classes(df):
    classes = df['class'].unique()
    
    lst = []
    for each in classes:
        count = df[df['class'] == each]['class'].size
        if count >= 5:
            lst.append(each)
    
    return pd.DataFrame(data= {'class': lst})


dicti = {'students':'A B C D E F G H I'.split(), 'class': "math english math biology math computer math math math".split()}

df = pd.DataFrame(data= dicti)
print(find_classes(df))