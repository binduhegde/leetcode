import pandas as pd
def find_student(df):
    return df[df.student_id == 101][['name', 'age']]


data = [[2, 'Bindu', 22], [101, 'bubu', 31]]
df = pd.DataFrame(data, columns= ['student_id', 'name', 'age'])

print(find_student(df))