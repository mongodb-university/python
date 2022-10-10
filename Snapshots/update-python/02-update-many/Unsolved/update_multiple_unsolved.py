"""Code for Python drivers course - Unit 2, Lesson 4.

Lesson title: Updating Documents in Python Applications

Learning objective:
- Update documents using update_one() and update_many()
"""

import os
import pprint

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

# Filter
select_accounts = {"account_type": "savings"}

# Update
add_transfer = {"$push": {"transfers_complete": "TR413308000"}}

# TODO: Write an expression that adds the transfer ID number to the 'tranfers_complete' list of each checking account. Assign the result of this update operation to a variable named `result`.


print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
