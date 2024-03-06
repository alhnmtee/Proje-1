from elasticsearch import Elasticsearch
from pymongo import MongoClient
from bson.json_util import dumps

# MongoDB'ye bağlanın
mongo_client = MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
mongo_db = mongo_client["yazlab"]
mongo_collection = mongo_db["kaynak"]

# Elasticsearch'e bağlanın
es = Elasticsearch('http://localhost:9200')

# MongoDB koleksiyonundaki belgeleri alın ve Elasticsearch endeksine ekleyin
for document in mongo_collection.find():
    document_id = document.pop('_id')  # _id alanını belgeden çıkarın
    es.index(index='your_elasticsearch_index', id=document_id, body=dumps(document))


print("Veri MongoDB'den Elasticsearch'e başarıyla aktarıldı.")

# Elasticsearch'te belirli bir başlıkta "Yazılım" olan ve belirli bir yazarı "Nazmiye" olan belgeleri arayın
result = es.search(index='your_elasticsearch_index', body={
    "query": {
        "bool": {
            "must": [
                
                {"match": {"authors": "Nazmiye"}}
            ]
        }
    }
})

# Sonuçları yazdırın
print("Arama Sonuçları:")
for hit in result['hits']['hits']:
    print(hit['_source'])
