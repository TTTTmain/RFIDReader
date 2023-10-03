import pymongo
from pymongo import MongoClient


database_name = "appdb"
collection1_name = "registeredUsers"
collection2_name = "newUsers"

# There is one database containing 2 collections
client = MongoClient('localhost', 27017)
db = client[database_name]

#collections are for newUsers and registeredUsers
collection_1 = db[collection1_name]
collection_2 = db[collection2_name]

doc1 = ({
    'name': 'Yumal',
    'ID': 30110602,
    'RFID': 'e200470cd6606821f02c0110',
    'permit': 'Blue',
    'plate': ['XY1-G1Y'] 
})

doc2 = ({
    'name': 'Tim',
    'ID': 12579638,
    'RFID': 'e200470cd6706821f02d0111',
    'permit': 'Red',
    'plate': ['TYT-X2D'] 
})

doc3 = ({
    'name': 'John',
    'ID': 35987260,
    'RFID': 'e200470d6de06821f9a40111',
    'permit': 'Blue',
    'plate': ['FVS-OP3'] 
})

doc4 = ({
    'name': 'Rob',
    'ID': 69803158,
    'RFID': 'e200470d6df06821f9a50114',
    'permit': 'Blue',
    'plate': ['RBK-40P'] 
})


#NEW inserting document into collection_1
result1 = collection_1.insert_one(doc1)
result2 = collection_1.insert_one(doc2)
result3 = collection_1.insert_one(doc3)
result4 = collection_1.insert_one(doc4)


#Find all documents inside the collection
documents = collection_1.find()
documents1 = collection_2.find()

#Print the database documents
print("The registered users: \n")
for reg_users in documents:
    print(reg_users)
    print('-' * 20)
    print("\n")


print("The new users: \n")
for new_user in documents1:
    print(new_user)
    print('-' * 20)
    print("\n")



## Adding a new user to Collection_2 using app sign-up










# # Define a filter to specify which document to remove
# filter_criteria = {"name": "Jhon"}  # Replace with your filter criteria

# # Remove a single document that matches the filter criteria
# result = collection_1.delete_many(filter_criteria)

# # Check if a document was deleted
# if result.deleted_count == 1:
#     print("Document deleted successfully.")
# else:
#     print("No matching document found.")

