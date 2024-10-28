import pandas as pd

def article_views(views):
    # create new_df with rows where author_id == viewer_id 
    # and storing only the author_id column in new_df
    new_df = views[(views['author_id'] == views['viewer_id'])][['author_id']]
    # dropping duplicate values in author_id column
    new_df = new_df.drop_duplicates(subset = ['author_id'])
    # sorting the author_id column
    new_df = new_df.sort_values(['author_id'])
    # rename author_id to id
    new_df = new_df.rename(columns = {'author_id': 'id'})
    return new_df

data = [[1,3,5], [1,3,6], [2,7,7], [2,7,6], [4,7,1], [3,4,4], [3,4,4]]
df = pd.DataFrame(data, columns = ['article_id', 'author_id', 'viewer_id'])

print(article_views(df))