from consolemenu import *
from consolemenu.items import *
import modules.movies
import modules.visualization

def MenuInit():

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
    menu_movies = SelectionMenu('')
    submenu_movies = SubmenuItem("Movies", menu_movies, menu)
    func_movies_search = FunctionItem('Recommend Movies Based On Title', modules.movies.Search)

    menu_data = SelectionMenu('')
    submenu_data = SubmenuItem("Data analysis", menu_data, menu)
    func_data_plot_by_genre = FunctionItem('Plot by genre', modules.visualization.plot_by_genre)
    
    func_data_plot_by_country = FunctionItem('Plot by country', modules.visualization.plot_by_country)

    # Once we're done creating them, we just add the items to the menu
    menu_movies.append_item(func_movies_search)
    menu_data.append_item(func_data_plot_by_genre)
    menu_data.append_item(func_data_plot_by_country)
    # menu.append_item(command_item)
    menu.append_item(submenu_movies)
    menu.append_item(submenu_data)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

