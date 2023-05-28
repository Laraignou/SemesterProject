import sqlite3 as sqlite
import pandas as pd
import singleton

# References:
# https://stackoverflow.com/questions/36519086/how-to-get-rid-of-unnamed-0-column-in-a-pandas-dataframe-read-in-from-csv-fil
# https://theleftjoin.com/how-to-write-a-pandas-dataframe-to-an-sqlite-table/

def create_recommender_database(dataset, database, table_name):
    con = sqlite.connect(database)   
    df = pd.read_csv(dataset, low_memory=True, index_col=0)
    df.to_sql(table_name, con, if_exists="replace", index=False)
    singleton.recommender_connection=con

create_recommender_database('project/resources/data/Dataset_Collection/recommender.csv',
'D:/GitHub/SemesterProject/project/resources/database/recommender.db', 'movies')