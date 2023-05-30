import sqlite3 as sqlite
import pandas as pd
from modules import singleton
# import modules.singleton


# References:
# https://stackoverflow.com/questions/36519086/how-to-get-rid-of-unnamed-0-column-in-a-pandas-dataframe-read-in-from-csv-fil
# https://theleftjoin.com/how-to-write-a-pandas-dataframe-to-an-sqlite-table/

def create_recommender_database(dataset, database, table_name):
    singleton.recommender_connection = sqlite.connect(database, check_same_thread=False)   

    df = pd.read_csv(dataset, low_memory=True, index_col=0)
    df.to_sql(table_name, singleton.recommender_connection, if_exists="replace", index=False)

def get_connection():
    return singleton.recommender_connection

# create_recommender_database('project/resources/data/Dataset_Collection/recommender.csv',
# 'project/resources/database/recommender.db', 'movies')
# get_connection()

def initialize_database():
    create_recommender_database('resources/data/Dataset_Collection/recommender.csv',
'resources/database/recommender.db', 'movies')
    print("Created recommender database.")