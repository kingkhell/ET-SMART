from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB client
client = MongoClient()

# Create or access a database named 'MyNewDatabase'
db = client['MyNewDatabase']

# Create or access a collection named 'employees'
employees = db['employees']

# Insert a new employee document
employee = {
    "id": "102",
    "name": "Sdd",
    "profession": "software engineer"
}

# Insert the employee into the 'employees' collection
employees.insert_one(employee)

# Update the employee's name
employees.update_one(
    {"id": "102"},  # Filter to find the document with id "102"
    {"$set": {"name": "fuck"}}  # Update the 'name' field
)

# Retrieve and print the updated document
pprint(employees.find_one({"id": "102"}))
