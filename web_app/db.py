from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://mongodb:27017/"))
db = client["final_project"]

"""
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Connected to MongoDB!")
except Exception as e:
    print("MongoDB connection error:", e)
"""
