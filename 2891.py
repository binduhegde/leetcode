import pandas as pd

def heavy_animals(df):
    # creating a new df by taking only the rows where the weight is > 100
    new_df = df[df['weight'] > 100]
    # sorting the new df in descending order
    new_df = new_df.sort_values(['weight'], ascending= False)
    # returning only the name column of the new df
    return new_df[['name']]


# creating a df
data = [['snake', '2', 10], ['buffalo', '20', 102], ['lion', '5', 100], ['gorilla', '50', 200], ['monkey', '4', 40], ['parrot', '2', 1], ['tiger', '3', 109], ['elephant', '25', 1000]]
df = pd.DataFrame(data, columns = ['name', 'age', 'weight'])

print(heavy_animals(df))