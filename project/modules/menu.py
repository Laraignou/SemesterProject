from consolemenu import *
from consolemenu.items import *
import modules.movies

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
    selection_menu_movies = SelectionMenu('', clear_screen=False)
    submenu_item_movies = SubmenuItem("Movies", selection_menu_movies, menu)
    function_item_movies_search = FunctionItem('Recommend Movies Based On Title', modules.movies.Search)
    function_item_movies_show_top10_global = FunctionItem('TOP 10 - Global', modules.movies.Show_Top10_Global_By_Title)
    function_item_movies_show_top10_global = FunctionItem('TOP 10 - Global', modules.movies.Show_Top10_Global_By_Genre)

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