import pandas as pd

# The bonus of an employee is 100% of their salary if the ID 
# of the employee is an odd number and the employee's name does not 
# start with the character 'M'. The bonus of an employee is 0 otherwise.
def calculate_bonus(df):
    # create new column with values all 0
    df['bonus'] = 0 
    # Calculate bonus based on the conditions
    df.loc[(df['employee_id'] % 2 != 0) & (~df['name'].str.startswith('M')), 'bonus'] = df['salary']
    # Select only the required columns and sort the result table by employee_id in ascending order
    result_df = df[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
    return result_df

# creating a df. salary is 1000 if they're qualified for bonus. 2000 otherwise
data = [[2, 'May', 2000], [3, 'Mary', 2000], [7, 'adi', 1000], [8, 'juan', 2000], [9, 'Ken', 1000]]
df = pd.DataFrame(data, columns = ['employee_id', 'name', 'salary'])
print(calculate_bonus(df))