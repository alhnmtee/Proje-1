from elasticsearch import Elasticsearch
from pymongo import MongoClient
from bson.json_util import dumps

# MongoDB'ye bağlanın
mongo_client = MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
mongo_db = mongo_client["yazlab"]
mongo_collection = mongo_db["kaynak"]

# Elasticsearch'e bağlanın
es = Elasticsearch('http://localhost:9200')

#Her veri atıldığnda çalışacak sadece :D:D:D:D
# MongoDB koleksiyonundaki belgeleri alın ve Elasticsearch endeksine ekleyin
# for document in mongo_collection.find():
#     document_id = document.pop('_id')  # _id alanını belgeden çıkarın
#     es.index(index='your_elasticsearch_index', id=document_id, body=dumps(document))


# result = es.search(index='your_elasticsearch_index', body={
#    "query": {
#        "bool": {
#            "must": [
#               # {"match": {"match_all"}},
#                {"match": {"type": "Araştırma"}}
#            ]
#        }
#    }
# })

result = es.search(index='your_elasticsearch_index', body={
   "query": {
       "bool": {
           "must": [
               {"match": {"title": "data"}}
           ]
       }
   },
   "_source": ["url"] # Sadece URL'leri getir
})

# URL'leri almak için döngü
urls = [hit['_source']['url'] for hit in result['hits']['hits']]
for url in urls:
    print(url)

#response = es.delete_by_query(index='your_elasticsearch_index', body={"query": {"match_all": {}}})
# Silinen belgelerin sayısını yazdırın
#print("Silinen Belgelerin Sayısı:", response['deleted'])

# Sonuçları yazdırın
# print("Arama Sonuçları:")
# for hit in result['hits']['hits']:
#     print(hit['_source'])
