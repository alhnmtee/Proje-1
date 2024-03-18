from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')
response = es.delete_by_query(index='your_elasticsearch_index', body={"query": {"match_all": {}}})
print("Silinen Belgelerin Sayısı:", response['deleted'])