import elasticsearch
from elasticsearch import helpers
import pymongo
from bson import ObjectId  # Import ObjectId from bson

# Connect to MongoDB
mongo_client = pymongo.MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
mongo_db = mongo_client["yazlab"]
mongo_collection = mongo_db["kaynak"]

# Connect to Elasticsearch
es = elasticsearch.Elasticsearch("http://localhost:9200")

# Define a function to retrieve data from MongoDB
def get_data_from_mongodb():
    for doc in mongo_collection.find():
        # Convert ObjectId to string
        doc["_id"] = str(doc["_id"])
        yield {
            "_index": "your_index_name",  # Specify your Elasticsearch index name
            "_source": doc
        }

# Use the helpers.bulk() function to insert data into Elasticsearch
try:
    success, _ = helpers.bulk(es, get_data_from_mongodb(), index="your_index_name", raise_on_error=True)
    print("Successfully indexed {} documents".format(success))
except Exception as e:
    print("Error:", e)
