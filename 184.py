import pandas as pd

def department_highest_salary(employee, department):
    dept_id = set(employee['departmentId'].to_list())

    result_df = {'Department':[], 'Employee':[], 'Salary':[]}

    for dept in dept_id:
        new_df = employee[employee['departmentId'] == dept]
        
        highest = new_df['salary'].max()
        highest_df = new_df[new_df['salary'] == highest]

        for ind in highest_df.index:
            department_id =highest_df['departmentId'][ind]
            dpt = department[department['id'] == int(department_id)]['name'].to_list()[0]

            result_df['Department'].append(dpt)
            result_df['Employee'].append(highest_df['name'][ind])
            result_df['Salary'].append(highest_df['salary'][ind])
    
    return pd.DataFrame(data=result_df)



# creating data
# employee_data = {'id': [1, 2, 3, 4, 5], 'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'], 'salary': ['70000', '90000', '80000', '60000', '90000'], 'departmentId': ['1', '1', '2', '2', '1']}
# employee = pd.DataFrame(data=employee_data)

# department_data = {'id':[1, 2], 'name':['IT', 'Sales']}
# department = pd.DataFrame(data= department_data)
employee_data = {'id': [1,4], 'name': ['Joe', 'Max'], 'salary': [60000,60000], 'departmentId': [1,2]}
employee = pd.DataFrame(data=employee_data)

department_data = {'id':[1, 2], 'name':['IT', 'HR']}
department = pd.DataFrame(data= department_data)

print(department_highest_salary(employee, department))