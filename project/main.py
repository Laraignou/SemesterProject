# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from modules import movies
import urllib.request
from urllib.request import urlopen
from tqdm import tqdm
import time
import os
from modules.database import create_recommender_database
from setup import *
from modules.singleton import singleton_init

singleton_init()
Download_and_Install_Libraries()

# def download_dataset():

#     url = "https://www.dropbox.com/s/s5yarta1lk6afz3/Dataset_Collection.zip?dl=1"
#     save_as = "project/resources/data/Dataset.zip"

#     # Download from URL
#     with urlopen(url) as file:
#         content = file.read()#.decode()

#     # Save to file
#     with open(save_as, 'wb') as download:
#         download.write(content)

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, save_as):
    print('Downloading dataset...')
    time.sleep(1)

    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, save_as, reporthook=t.update_to)

# full path doesnt work for CMD therefore "../../../"
download_url(url="https://www.dropbox.com/s/s5yarta1lk6afz3/Dataset_Collection.zip?dl=1", save_as ="../../../Dataset.zip")

time.sleep(1)
os.system('cls')
print('Opening application...')
time.sleep(1)

def initialize_database():
    create_recommender_database('project/resources/data/Dataset_Collection/recommender.csv',
'D:/GitHub/SemesterProject/project/resources/database/recommender.db', 'movies')
    print("Created recommender database.")
    
def mainInit():

    # Create the menu
    menu = ConsoleMenu("Movie Recommendation System - Statictics and visualization", "By Carlo & Frederik", clear_screen=False)

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    # menu_item = MenuItem("Menu Item")

    # A FunctionItem runs a Python function when selected
    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu

    # A CommandItem runs a console command
    # command_item = CommandItem("Run a console command",  "touch hello.txt")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu_movies = SelectionMenu('', clear_screen=False)
    submenu_item_movies = SubmenuItem("Movies", selection_menu_movies, menu)
    function_item_movies_search = FunctionItem('Recommend Movies Based On Title', movies.Search)
    function_item_movies_show_top10_global = FunctionItem('TOP 10 - Global', movies.Show_Top10_Global_By_Title)
    function_item_movies_show_top10_global = FunctionItem('TOP 10 - Global', movies.Show_Top10_Global_By_Genre)

    selection_menu_stats_and_visuals = SelectionMenu(["Statictics", "Visualize"])
    submenu_item_Stats_and_Visual = SubmenuItem("Data analysis", selection_menu_stats_and_visuals, menu)


    # Once we're done creating them, we just add the items to the menu
    selection_menu_movies.append_item(function_item_movies_search)
    selection_menu_movies.append_item(function_item_movies_show_top10_global)
    # menu.append_item(command_item)
    menu.append_item(submenu_item_movies)
    menu.append_item(submenu_item_Stats_and_Visual)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

initialize_database()
mainInit()

    