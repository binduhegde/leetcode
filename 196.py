import pandas as pd

def drop_dup(person):
    person.sort_values(by=['id'], inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)
    return person


df = {'id':[1,3,2], 'email':['bindu@gmail.com', 'bubu@gmail.com', 'bindu@gmail.com']}
print(drop_dup(pd.DataFrame(data=df)))