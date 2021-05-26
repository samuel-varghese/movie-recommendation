import pandas as pd 
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
ratings = pd.read_csv("toy_dataset.csv",index_col=0)
ratings=ratings.fillna(0)
#print(ratings)

def standardize(row):
    new_row=(row-row.mean())/(row.max()-row.min())
    return new_row
ratings_std=ratings.apply(standardize)
print(ratings_std)
item_similarity=cosine_similarity(ratings_std.T)
#print(item_similarity)
item_similarity_df=pd.DataFrame(item_similarity,index=ratings.columns,columns=ratings.columns)
#print(item_similarity_df)

def get_similar_movies(movie_name,user_rating):
        similar_score=item_similarity_df[movie_name]*(user_rating-2.5)
        similar_score=similar_score.sort_values(ascending=False)
        
        return similar_score
#print(get_similar_movies("romantic1",1))

action_lover=[("action1",5),("action2",4),("romantic2",1)]

similar_movies=pd.DataFrame()
for movie,rating in action_lover:
    similar_movies=similar_movies.append(get_similar_movies(movie,rating),ignore_index=True)
    
similar_movies.head
#print(similar_movies.sum().sort_values(ascending=False))
#print(similar_movies)