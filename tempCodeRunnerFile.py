from json import dumps
from pyparsing import html_comment
import requests
import pymongo
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
#TODO ElasticSearch araştırdım bi hesap açtım güya bir şeyler denedim ama sync aşaması hata verdi tamamlayamadım.Yapamadım


client = pymongo.MongoClient("mongodb+srv://yazlab:yazlab@cluster0.ier7hbc.mongodb.net/")
db = client["yazlab"]
collection = db["kaynak"]

es = Elasticsearch('http://localhost:9200')
for document in collection.find():
        document_id = document.pop('_id')  # _id alanını belgeden çıkarın
        es.index(index='your_elasticsearch_index', id=document_id, body=dumps(document))