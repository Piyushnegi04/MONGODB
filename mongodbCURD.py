from pymongo import MongoClient
##to establish DB conection
client = MongoClient("mongodb://localhost:27017/")
##create DB if not exist or access the DB
mydatabase = client["instadb"]
##create collection if not exist or acess the collection
mycollection = mydatabase["users"]

##insert 1/many users
# user = [{"name":"avi negi", "email":"p@gmail.com"},{"name":"piyush negi", "email":"n@gmail.com"},{"name":"negi", "email":"a@gmail.com"}]
# mycollection.insert_many(user)

##access all the record from MONGODB
# data = mycollection.find() 
# for i in data:
#     print(i)

##to access the specific record
# data = mycollection.find_one({"email":"p@gmail.com"})
# print(data)

##to delete the specific document
# mycollection.delete_one({"email":"a@gmail.com"})
# data = mycollection.find() 
# for i in data:
#     print(i)

##to sort the data
# data = mycollection.find().sort("name",-1) ##-1 for reverse order
# for i in data:
#     print(i)

##update the record 1/many
# mycollection.update_one({"email":"an@gmail.com"},{"$set":{"email":"negi@gmail.com"}})
# data = mycollection.find()
# for i in data:
#     print(i)

##to drop/delete the whole collection
#mycollection.drop()