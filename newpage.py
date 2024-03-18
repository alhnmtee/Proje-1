from elasticsearch import Elasticsearch
from pymongo import MongoClient


mongo_client = MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
mongo_db = mongo_client["yazlab"]
mongo_collection = mongo_db["kaynak"]

def get_newpage_data(filter_data):
    print("Received filter data:", filter_data)
    # Elasticsearch bağlantısı
    es = Elasticsearch('http://localhost:9200')
    result = es.search(index='your_elasticsearch_index', body={
   "query": {
       "bool": {
           "must": [
               {"term": {"title.keyword": filter_data}}
           ]
       }
   }
})
    bilgi = result['hits']['hits'][0]['_source']
    
    print("Elasticsearch sorgusu sonucu:", result)
    return bilgi


