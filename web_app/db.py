from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

"""
TODO: Uncomment this part once we have our URI and DBNAME set up

uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGO_DBNAME")

# Display error message if mongoDB environment is not set up
if not uri or not db_name:
    error_message = "MongoDB environment is not set up. Please check your environment variables."
    app.logger.error(error_message)
    raise EnvironmentError(error_message)

# Create a new client and connect to the server
client = MongoClient(uri)
db = client[db_name]
"""

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://mongodb:27017/"))
db = client.test


"""
TODO: Uncomment once mongoDB environment is set up
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Connected to MongoDB!")
except Exception as e:
    print("MongoDB connection error:", e)
"""
