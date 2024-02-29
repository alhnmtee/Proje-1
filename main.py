from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Anani Sikeyim ! "

@app.route('/api/anani' , methods=['GET'])
def test():
    return jsonify({"la ": "o"})

if __name__ == '__main__':
    app.run(debug=True)