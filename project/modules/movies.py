from modules.recommender import get_recommendations_by_title
from modules.singleton import get_database_connection

def Search():
    print('Enter movie title: ')
    text = input("")
    print("Loading movies...")
    print(get_recommendations_by_title(text, get_database_connection(), "movies"))
    
def Show_Top10_Global_By_Title():
    print('test')
    
def Show_Top10_Global_By_Genre():
    print('test')

def Show_Top10_By_Country():
    print('test')