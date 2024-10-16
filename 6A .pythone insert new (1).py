from pymongo import MongoClient
import pprint

# Connect to MongoDB
client = MongoClient()

# Create or access a database (no spaces in the name)
db = client["MyNewDatabase"]

# Create an employee document
employee = {
    "id": "102",
    "name": "zee",
    "profession": "Software Engineer"
}

# Access the collection (table)
employees = db.employees

# Insert the employee document into the collection
employees.insert_one(employee)

# Find and print one document from the collection
pprint.pprint(employees.find_one())
