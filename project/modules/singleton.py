import time

def singleton_init():
    global recommender_connection
    print("Initializing DB connection..!")
    time.sleep(2)
    
def get_database_connection():
    return recommender_connection