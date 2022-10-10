"""Code for Python drivers course - Unit 3, Lesson 3

Lesson title: Using MongoDB aggregation stages with Python: $sort and $project

Learning objectives:
- Build an aggregation pipeline using Python
- Identify the stages ($sort, $project) of an aggregation pipeline
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

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Return the account type, original balance, and balance converted to Great British Pounds (GBP) of all checking accounts with an original balance of greater than $1,500 US dollars, in order from highest original balance to lowest.

# To calculate the balance in GBP, divide the original balance by the conversion rate.
conversion_rate_usd_to_gbp = 1.3

# TODO 1: Select checking accounts with balances of more than $1,500.


# TODO 2: Organize documents in order from highest balance to lowest.


# TODO 3: Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP). Name the new field "gbp_balance"


# TODO 4: Create an aggegation pipeline containing the four stages created above


# TODO 5: Perform an aggregation on 'pipeline'.


print(
    "Account type, original balance and balance in GDP of checking accounts with original balance greater than $1,500, in order from highest original balance to lowest: "
)

for item in results:
    pprint.pprint(item)

client.close()
