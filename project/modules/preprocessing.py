import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ast import literal_eval
import zipfile

def Unzip_Dataset():
        
        with zipfile.ZipFile('Project/Resources/Dataset/Dataset_Collection.zip', 'r') as zip_ref:
                zip_ref.extractall('Project/Resources/Dataset/')

Unzip_Dataset()

def Data_Cleaning():

    df = pd.read_csv('Project/Resources/Dataset/Dataset_Collection/movies_metadata.csv', low_memory=False)
    # print(df.isnull())
    # print(df.isnull().sum())
    # print(df.shape)
    # df.info()
    # print(df.head(10))
    
    duplicated_data = df[df.duplicated()]
    # print(duplicated_data.head(10))
    drop_df = ["homepage", "poster_path", "video", "imdb_id", "overview", "original_title", "spoken_languages", "tagline"]
    df = df.drop(drop_df, axis=1) # drops the selected columns
    df = df.drop_duplicates(keep='first') # removes the duplicates from existing dataframe
    df.dropna(how="all",inplace=True) # if each column is NaN or null in a row, drops this row

    # print(df.shape)
    
    count_missing_title_in_rows = df['title'].isna().sum()
    # print(count_missing_title_in_rows)

    df.dropna(subset=["title"], inplace=True)
    # print(df.shape)

    df["id"] = pd.to_numeric(df['id'], errors='coerce', downcast="integer")
    df["popularity"] =pd.to_numeric(df['popularity'], errors='coerce', downcast="float") 
    df["budget"] =pd.to_numeric(df['budget'], errors='coerce', downcast="float") 
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['release_year'] = df['release_date'].dt.year

    df['belongs_to_collection'] = df['belongs_to_collection'].fillna("None")
    df['belongs_to_collection'] = (df['belongs_to_collection'] != "None").astype(int)

    # print(df["adult"].value_counts())
    df.drop(["adult"], inplace=True, axis=1)
    
    # df.info()

    df["status"].fillna(df["status"].value_counts().idxmax(), inplace=True)
    df["runtime"] = df["runtime"].replace(0, np.nan)
    df["runtime"].fillna(df["runtime"].mean(), inplace=True) 

    df.dropna(subset=["release_date"],inplace=True)
    df.dropna(subset=["original_language"],inplace=True)

    # converts json list to list of inputs (from the label specified with 'wanted' parameter)
    def json_to_arr(cell, wanted = "name"): 
        cell = literal_eval(cell)
        if cell == [] or (isinstance(cell, float) and cell.isna()):
            return np.nan
        result = []
        counter = 0
        for element in cell:
            if counter < 3:
                result.append(element[wanted])
                counter += 1
            else:
                break
        return result[:3]


    df[['genres']] = df[['genres']].applymap(json_to_arr)
    df[['production_countries']] = df[['production_countries']].applymap(lambda row: 
                                                                        json_to_arr(row, "iso_3166_1"))
    df[['production_companies']] = df[['production_companies']].applymap(json_to_arr)

    # print(df[['genres', 'production_countries','production_companies']])

    df['budget'] = df['budget'].replace(0 , np.nan)
    df['revenue'] = df['revenue'].replace(0 , np.nan)


    # print("Number of rows with budget < 100: ", len((df[(df["budget"].notna())&(df["budget"] < 100)])))
    # print("Number of rows with budget > 100 and < 1000: ", len(df[(df["budget"].notna())&(df["budget"] > 100)
    #                                                             &(df["budget"] < 1000)]))
    # print("Number of rows with budget > 1000 and < 10000: ", len(df[(df["budget"].notna())&(df["budget"] > 1000)
    #                                                             &(df["budget"] < 10000)]))

    def scale_money(num):
        if num < 100:
            return num * 1000000
        elif num >= 100 and num < 1000:
            return num * 10000
        elif num >= 1000 and num < 10000:
            return num *100
        else:
            return num

    df[['budget', 'revenue']] = df[['budget', 'revenue']].applymap(scale_money)

    null_counts = df.isna().sum()
    # print(null_counts)

    # print("NaN Genres Count: ", len(df[df["genres"].isna()]))
    # print("NaN Revenue Count: ", len(df[df['revenue'].isna()])) 
    # print("NaN Budget Count: ", len(df[df['budget'].isna()])) 
    # print("NaN Production Company Count: ", len(df[df["production_companies"].isna()]))
    # print("NaN Production Country Count: ", len(df[df["production_countries"].isna()]))

    # returns the values and occurance times or "limiter" amount of different parameters in a 2D list
    
    def list_counter(col, limiter = 9999, log = True):
        result = dict()
        for cell in col:
            if isinstance(cell, float):
                continue
            for element in cell:
                if element in result:
                    result[element] += 1
                else:
                    result[element] = 1
        if log:
            print("Size of words:", len(result))
        result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
        if log:
            print("Sorted result is:")
        counter = 1
        sum_selected = 0
        total_selected = 0
        rest = 0
        returned = []
        for i in result: 
            if counter > limiter:
                total_selected += result[i]
            else:
                counter += 1
                sum_selected += result[i]
                total_selected += result[i]
                if log:
                    print(result[i], " - ", i) 
                returned.append([i, result[i]])
        if log:
            print("Covered:", sum_selected, "out of", total_selected, "\n")
        return returned
    
    genres_occur = list_counter(df["genres"].values, log=False)
    genres = pd.DataFrame.from_records(genres_occur, columns=["genres", "count"])
    genres.plot(kind = 'bar', x="genres", title='Genre')
    plt.savefig('Project/Resources/Figures/plot_figure_1.png')
    
    countries_occur = list_counter(df["production_countries"].values, log=False)
    countries = pd.DataFrame.from_records(countries_occur, columns=["countries", "count"])
    countries.head(20).plot(kind = 'bar', x="countries", title='Countries')
    plt.savefig('Project/Resources/Figures/plot_figure_2.png')
    
Data_Cleaning()


    # df.info()
    # print(df)
    # df.plot(kind='bar')
    
    # print(df)
    # print(type(df))
    
    # df = str(pd.read_csv('TMDB_5000/tmdb_5000_movies.csv'))
    # print(df)
    # df = df.lower()
    # print(df)
    # print(type(df))