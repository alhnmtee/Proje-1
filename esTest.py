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

# index_mapping = {
#     "mappings": {
#         "properties": {
#             "date": {
#                 "type": "keyword"  # Date alanını keyword olarak tanımla
#             }
#         }
#     }
# }
# es.indices.create(index='your_elasticsearch_index', body=index_mapping)
for document in mongo_collection.find():
    document_id = document.pop('_id')  # _id alanını belgeden çıkarın
    es.index(index='your_elasticsearch_index', id=document_id, body=dumps(document))



#print("Elasticsearch endeksine başarıyla veri eklendi.")
# result1 = es.search(index='your_elasticsearch_index', body={
#    "query": {
#        "bool": {
#            "must": [
#               # {"match": {"match_all"}},
#                {"match": {"type": "Araştırma"}}
#            ]
#        }
#    }
# })
# print("Arama Sonuçları:")
# for hit in result1['hits']['hits']:
#     print(hit['_source'])
    

result = es.search(index='your_elasticsearch_index', body={
   "query": {
       "bool": {
           "must": [
               #{"match": {"match_all"}},
               #{"match": {"title": "health"}}
           ]
       }
   },
   #"_source": ["url"] # Sadece URL'leri getir
   "size": 300
})

# URL'leri almak için döngü
titles = [hit['_source']['title'] for hit in result['hits']['hits']]
#for title in titles:
    #print(title)   

# response = es.delete_by_query(index='your_elasticsearch_index', body={"query": {"match_all": {}}})
# # Silinen belgelerin sayısını yazdırın
# print("Silinen Belgelerin Sayısı:", response['deleted'])

#Sonuçları yazdırın
# print("Arama Sonuçları:")
# for hit in result['hits']['hits']:
#     print(hit['_source'])
