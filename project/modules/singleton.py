
def singleton_init():
    global recommender_connection
    print("Singleton ready!")
    
def get_database_connection():
    return recommender_connection