import scrape
from flask_cors import CORS
from flask import Flask, jsonify, request
import esTest
from bson.json_util import dumps

app = Flask(__name__)

CORS(app)

@app.route('/api/searchresults')
def test():
    return (dumps(esTest.urls))

@app.route('/api/searchwords', methods=['POST'])
def receive_data():
    data = request.json  
    received_text = data.get('text')  
    print('Received text:', received_text)
    scrape.dergiParkScraping(received_text,1)
    return jsonify({'message': 'Data received successfully'})
    


if __name__ == '__main__':
    app.run(debug=True)
    