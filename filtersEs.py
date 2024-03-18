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
                "should": [],
                "must": []
            }
        },
        "size": 100,
        "sort": [{"date": {"order": filter_data['sortOrder']}}]  # Sıralama yapılacak alan ve sıralama tipi (asc/desc)
    }

    print("Filter data:", filter_data)

    if filter_data['type']:
        query["query"]["bool"]["must"].append({"match": {"type": filter_data['type']}})
    if filter_data['title']:
        title_should = {"match": {"title": filter_data['title']}}
        summary_should = {"match": {"summary": filter_data['title']}}
        query["query"]["bool"]["should"].append(title_should)
        query["query"]["bool"]["should"].append(summary_should)
    # if filter_data['date']:
    #     query["query"]["bool"]["must"].append({"match": {"date": filter_data['date']}})
    if filter_data['date']:
        date_parts = filter_data['date'].split('-')
        if len(date_parts) == 1:  
            year = date_parts[0]
            start_date = f"{year}-01-01"
            end_date = f"{year}-12-31"
            query["query"]["bool"]["must"].append({"range": {"date": {"gte": start_date, "lte": end_date}}})
        elif len(date_parts) == 2:  
            start_year = date_parts[0]
            end_year = date_parts[1]
            start_date = f"{start_year}-01-01"
            end_date = f"{end_year}-12-31"
            query["query"]["bool"]["must"].append({"range": {"date": {"gte": start_date, "lte": end_date}}})

    if filter_data['keywords']:
        query["query"]["bool"]["must"].append({"match": {"keywords": filter_data['keywords']}})
    if filter_data['authors']:
        query["query"]["bool"]["must"].append({"match": {"authors": filter_data['authors']}})

    result = es.search(index='your_elasticsearch_index', body=query)
    #print("Elasticsearch sorgusu sonucu:", result)
    sources = [hit['_source'] for hit in result['hits']['hits']]
    #print("Filtered data:", sources)
    return sources
