import pandas as pd


# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel

#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer



# Function that takes in movie title as input and outputs most similar movies
def get_recommendations_by_title(title, database_connection, tableName):
    
    df = pd.read_csv('project/resources/data/Dataset_Collection/recommender.csv', low_memory=False)
    # df = pd.read_csv('resources/data/Dataset_Collection/recommender.csv', low_memory=False) 
    df = pd.read_sql_query("SELECT * FROM " + tableName, database_connection)
    
    #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')
    
    #Replace NaN with an empty string
    df.loc['overview'] = df['overview'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(df['overview'].values.astype('U'))

    #Output the shape of tfidf_matrix
    #tfidf_matrix.shape
    
    # # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()

    # # Get the index of the movie that matches the title
    idx = indices[title]

    # # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # # Get the movie indicescl
    movie_indices = [i[0] for i in sim_scores]

    # # Return the top 10 most similar movies
    return df['title'].iloc[movie_indices]

# print(get_recommendations_by_title("Avatar", singleton.recommender_connection, 'movies'))