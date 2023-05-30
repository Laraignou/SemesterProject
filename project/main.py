# Import the necessary packages
import time
import os
from setup import *
from modules.download_data import *
from modules.unzip import *
from modules.preprocessing import *
from modules.recommender_cleanup import *
from modules.singleton import *
from modules.database import *
from modules.menu import *

def first_run():
    user_input = input('Is this your first run? (Y/N): ')

    if user_input.lower() == 'y':
        Download_and_Install_Libraries()
        download_url(url="https://www.dropbox.com/s/s5yarta1lk6afz3/Dataset_Collection.zip?dl=1", save_as ="project/resources/data/Dataset.zip")
        # download_url(url="https://www.dropbox.com/s/s5yarta1lk6afz3/Dataset_Collection.zip?dl=1", save_as ="resources/data/Dataset.zip")
        Unzip_Dataset()
        Data_Cleaning()
        cleanUpDataset('project/resources/data/Dataset_Collection/movies_metadata.csv', 'project/resources/data/Dataset_Collection/recommender.csv')
        # cleanUpDataset('resources/data/Dataset_Collection/movies_metadata.csv', 'resources/data/Dataset_Collection/recommender.csv')
        singleton_init()
        create_recommender_database('project/resources/data/Dataset_Collection/recommender.csv',
        'project/resources/database/recommender.db', 'movies')
        # create_recommender_database('resources/data/Dataset_Collection/recommender.csv',
        # 'resources/database/recommender.db', 'movies')
        get_connection()
        initialize_database()
        print('Opening application...')
        time.sleep(1)
        os.system('cls')
        MenuInit()

    elif user_input.lower() == 'n':
        print('Opening application...')
        time.sleep(1)
        os.system('cls')
        MenuInit()
    else:
        print('Type (Y)es or (N)o')
        first_run()

first_run()









    