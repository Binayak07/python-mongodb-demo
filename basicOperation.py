import pymongo
client_cloud = pymongo.MongoClient("mongodb+srv://root:root@cluster0.9bpnr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client_cloud.test

#Creating a database/collection
database = client_cloud["myFirstDB"]

#Checking database names
dbList = client_cloud.list_database_names()

#Creating a Collections
collection = client_cloud["ineuron"]

#Inserting one/bulk document(s)
# record={"course":"Full Stack Data Science", "duration":"1 Year","fees":18000}
# record1={"course":"Full Stack Data Science", "duration":"2 Years","fees":10000}
# record2={"course":"Full Stack Data Science", "duration":"1 Year","fees":18000,"taughtby":"Sudhanshu Kr."}
# record5 = {"list":[1,2,"Hii",True]}
# record6 = {"list":[1,2,"Hii",True]}
# database["courses"].insert_one(record)
# record3={"course":"Full Stack Data Science","student":"Binayak","duration":"1 Year","fees":18000,"taughtby":"Sudhanshu Kr."}
# insertedIds = database["courses"].insert_many([record5,record6]).inserted_ids
# for id in enumerate(insertedIds):
#     print(id[1])

# find all data
allData = database["courses"].find({})
for record in allData:
    print(record)
# find one on condition
print("********************")
con = {"student":"Binayak","taughtby":"Sudhanshu Kr."}
foundData = database["courses"].find_one(con)
print('1 ===: ',foundData)
print("********************")
con = {"fees":{"$gt":17000}}
foundData = database["courses"].find(con)
for record in foundData:
    print("2 ===: ",record)
print("********************")
con = {"fees":{"$lt":18000}}
foundData = database["courses"].find(con)
for record in foundData:
    print("3 ===: ",record)
print("********************")
con = {"fees":{"$eq":18000}}
foundData = database["courses"].find(con)
for record in foundData:
    print("4 ===: ",record)
print("********************")
con = {"fees":{"$gte":18000}}
foundData = database["courses"].find(con)
for record in foundData:
    print("5 ===: ",record)
print("********************")
condel = {"_id":"612426e68134e43329b79b66"}
database["courses"].delete_one(condel)
print("Data Deleted")
print("********************")
record1={"_id":12,"name":"Richa","age":26,"gender":"female"}
record2={"_id":11,"name":"Binayak","age":29,"gender":"male"}
# condel = {"_id":{"$gte":11}}
# database["courses"].delete_many(condel)
print("Data Deleted")
print("********************")
# record1={"_id":14,"name":"Richa","age":26,"gender":"female"}
# record2={"_id":20,"name":"Binayak","age":29,"gender":"male"}
# database["courses"].insert_many([record1,record2])
database["courses"].update_many({"_id":{"$gte":14}},{"$set":{"address":"dhanbad"}},True)
"""
    Notes: Here, 'database' variable refers to the "myFirstDB" database and database["courses"] refers to the courses collections under the database.
"""