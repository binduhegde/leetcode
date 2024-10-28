import pandas as pd

def nth_highest(df, n):
    # bacause df is 0 indexed
    n -= 1
    # sorting the df and removing duplicates
    df = df['salary'].sort_values(ascending= False).drop_duplicates()

    # to have the nth_highest as None is n is negative or more than the len of the df
    if n in range(len(df)):
        highest = df.iloc[n]
    else:
        highest = None

    # creating a new df and returning it. n+1 to change it to original n value
    return pd.DataFrame(data = {f"getNthHighestSalary({n+1})":[highest]})






details = {
    'name': ['Ankit'], #'Aishwarya', 'Shaurya', 'Shivangi'],
    'salary': [5000]#, 25000, 25000, 21000],
}

# creating a Dataframe object
df = pd.DataFrame(details)


print(nth_highest(df, 1))