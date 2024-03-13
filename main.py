import scrape
from flask_cors import CORS
from flask import Flask, jsonify, request
import esTest
import filtersEs
import newpage
from bson.json_util import dumps


app = Flask(__name__)

CORS(app)

@app.route('/api/searchresults')
def test():
    #return esTest
    return (dumps(esTest.titles))

@app.route('/api/searchwords', methods=['POST'])
def receive_data():
    data = request.json  
    received_text = data.get('text')  
    print('Received text:', received_text)
    scrape.dergiParkScraping(received_text,1)
    return jsonify({'message': 'Data received successfully'})
    

@app.route('/api/filters', methods=['POST'])
def filter_data():
     data = request.json
     print("Received filter data:", data)
     veri= filtersEs.run_elasticsearch_query(data)
     #print("Filtered data:", veri)
     return jsonify(veri)
     
@app.route('/api/url', methods=['POST'])
def url_data():
    data = request.json
    data = data.get('text')
    cleaned_url = data.replace('/article/', '').replace('%20', ' ')
    #print("Cleaned URL:", cleaned_url)
    bilgi = newpage.get_newpage_data(cleaned_url)
    return jsonify({'message': bilgi})
    

if __name__ == '__main__':
    app.run(debug=True)
    