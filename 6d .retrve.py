from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['your_database_name']
employees = db.employees

result = employees.find_one({"id": 102})
print("Retrieved Employee:", result)
