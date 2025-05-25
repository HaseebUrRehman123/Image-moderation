from pymongo import MongoClient
from .config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.image_moderation
tokens_collection = db.tokens
