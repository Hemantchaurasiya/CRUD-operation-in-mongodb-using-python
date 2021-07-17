import pymongo

class Db:
    #database connction
    def __init__(self):
        #making the connection from the mongodb database
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        #getting the database from mongodb
        self.db = client['test']
        #getting the collecion from the database 
        self.collection = self.db['user']
        
    
    #insert the user data
    def insert_user(self,user_data):
        self.collection.insert_one(user_data)

    def fetch_one(self,user_id):
        user_data = self.collection.find_one({'_id':user_id})
        return user_data

    def fetch_all(self):
        users_data = self.collection.find()
        return users_data

    #update the user
    def update_user(self,user_id,user):
        self.collection.update_one({'_id':user_id},{"$set":user})

    #delete the user
    def delete_user(self,user_id):
        self.collection.delete_one({'_id':user_id})
    
