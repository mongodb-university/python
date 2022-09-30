"""Code for Python drivers course - Unit 2, Lesson 2.

Lesson title: Inserting a Document in a Python Application

Learning objective:
- Create documents using insert_one() and insert_many()
"""

import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow(),
}

# TODO: Write an expression that inserts the 'new_account' document into the 'accounts' collection. Assign the result of the insert operation to a variable named 'result'.


document_id = result.inserted_id
print(f"_id of inserted document: {document_id}")

client.close()
