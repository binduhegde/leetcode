import pandas as pd 

def second_highest(df):
    highest = df['salary'].max()
    df.drop(df[df['salary'] == highest].index, inplace= True)
    
    new_highest = df['salary'].max()
    new_data = {'SecondHighestSalary': [new_highest]}
    new_df = pd.DataFrame(data= new_data)
    return new_df


    # # another approach by sorting the df first. takes more time
    # new_df = df['salary'].sort_values(ascending=False).drop_duplicates()
    # if len(new_df) > 1:
    #     value = new_df.iloc[1]
    # else:
    #     value = None

    # return pd.DataFrame(data= {'SecondHighestSalary': [value]})



# dictionary with list object in values
details = {
    'name': ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    'salary': [25000, 25000, 22000, 21000],
}

# creating a Dataframe object
df = pd.DataFrame(details)


print(second_highest(df))