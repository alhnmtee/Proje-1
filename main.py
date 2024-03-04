import scrape
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)

CORS(app)

@app.route('/api/searchresults')
def test():
    return jsonify({'la': 'le'})

@app.route('/api/searchwords', methods=['POST'])
def receive_data():
    data = request.json  # Get the JSON data from the request body
    received_text = data.get('text')  # Extract the 'text' field
    # Do something with the received text
    print('Received text:', received_text)
    scrape.dergiParkScraping(received_text,1)
    return jsonify({'message': 'Data received successfully'})
    


if __name__ == '__main__':
    app.run(debug=True)
    