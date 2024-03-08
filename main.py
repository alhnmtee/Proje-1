import scrape
from flask_cors import CORS
from flask import Flask, jsonify, request
<<<<<<< Updated upstream
=======
import esTest
import filtersEs
from bson.json_util import dumps
>>>>>>> Stashed changes


app = Flask(__name__)

CORS(app)

@app.route('/api/searchresults')
def test():
    return jsonify({'la': 'le'})

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
     filtersEs.run_elasticsearch_query(data)
     return jsonify({'message': 'Filter data received successfully'})
     

if __name__ == '__main__':
    app.run(debug=True)
    