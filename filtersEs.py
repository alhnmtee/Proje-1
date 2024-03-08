from elasticsearch import Elasticsearch
from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
mongo_db = mongo_client["yazlab"]
mongo_collection = mongo_db["kaynak"]

def run_elasticsearch_query(filter_data):
    
    es = Elasticsearch('http://localhost:9200')

    
    query = {
        "query": {
            "bool": {
                "must": []
            }
        },
       
    }

    if filter_data['type']:
        query["query"]["bool"]["must"].append({"match": {"type": filter_data['type']}})
    if filter_data['title']:
        query["query"]["bool"]["must"].append({"match": {"title": filter_data['title']}})
    if filter_data['date']:
        query["query"]["bool"]["must"].append({"match": {"date": filter_data['date']}})
    if filter_data['keywords']:
        query["query"]["bool"]["must"].append({"match": {"keywords": filter_data['keywords']}})

    
    result = es.search(index='your_elasticsearch_index', body=query)
    print("Elasticsearch sorgusu sonucu:", result)


