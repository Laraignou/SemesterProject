import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

def generate_indicies(df, title):
    
    try:
        #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        tfidf = TfidfVectorizer(stop_words='english')
        
        df2 = df.copy()
        
        # #Replace NaN with an empty string
        df2.loc['overview'] = df2['overview'].fillna('')

        #Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(df2['overview'].values.astype('U'))

        #Output the shape of tfidf_matrix
        #tfidf_matrix.shape
        
        # Compute the cosine similarity matrix
        # Warning: Will consume big amount of ram if the dataframe has too many objects!
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        
        indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

        # Get the index of the movie that matches the title
        idx = indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the movie indicescl
        movie_indices = [i[0] for i in sim_scores]

        # # Return the top 10 most similar movies
        return df2['title'].iloc[movie_indices]
    except (KeyError, IndexError):
        return None

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations_by_title(title, database_connection, tableName):
    
    df = pd.read_csv('project/resources/data/Dataset_Collection/recommender.csv', low_memory=False)
    # df = pd.read_csv('resources/data/Dataset_Collection/recommender.csv', low_memory=False) 
    #df = pd.read_sql_query("SELECT * FROM " + tableName + " LIMIT 1000", database_connection)

    df2 = df.copy()
    df2 = df.iloc[0:0]
    
    # We need to split the dataframe into chunks
    # to ensure the recommmender/TfidfVectorizer algorithm
    # does not consume too much ram due to linear_kernel.
    
    # Sweet spot for relative good result is: 3 but 2 for optimal result.
    splitted = np.array_split(df, 3)
    for df1 in splitted:
        df2 = pd.concat([df1], ignore_index=True)
        result = generate_indicies(df2,title)
        if(result is not None): return result
    return "No movies found."

#print(get_recommendations_by_title("Toy Story", None, 'movies'))
#print(get_recommendations_by_title("Avatar", None, 'movies'))
#print(get_recommendations_by_title("The Dark Knight Rises", None, 'movies'))