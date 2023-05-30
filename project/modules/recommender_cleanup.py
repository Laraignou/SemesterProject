import pandas as pd

def cleanUpDataset(dataset, output):
    # Keep the following columns we need.
    keep_columns = ['id', 'title', 'overview', 'tagline']
    
    # Now read the entire dataset.
    df = pd.read_csv(dataset, low_memory=False, index_col=0)
    
    # Do cleaning.
    df = df[keep_columns]
    df = df.drop_duplicates(keep='first') # removes the duplicates from existing dataframe
    df.dropna(how="all",inplace=True) # if each column is NaN or null in a row, drops this row
    
    # Finally save the changes.
    df.to_csv(output)
    #print(df.info())