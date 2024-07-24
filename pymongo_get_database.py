from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
def get_database():
    
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #password = os.getenv('PASSWORD')
   CONNECTION_STRING = f"mongodb://localhost:27017/"
   database_name = "myFirstDatabase"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
#    db = client[database_name]
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
