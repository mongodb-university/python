"""Code for Python drivers course - Unit 3, Lesson 2.

Lesson title: Using MongoDB aggregation stages with Python: $match and $group

Learning objectives:
- Build an aggregation pipeline using Python
- Identify the stages ($match, $group) of an aggregation pipeline
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

# Calculate the average balance of checking and savings accounts with balances of less than $1000.

# TODO 1: Select accounts with balances of less than $1000.


# TODO 2: Separate documents by account type and calculate the average balance for each account type.


# TODO 3: Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.


# TODO 4: Perform an aggregation on 'pipeline'.


print(
    "Average balance of checking and savings accounts with balances of less than $1000:"
)

for item in results:
    pprint.pprint(item)

client.close()
