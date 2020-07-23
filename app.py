from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from banana import load_bananas, get_random_bananas

bananas = load_bananas('banana.ndjson')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def get_bananas():
    """ Returns 50 bananas """

    drawings = get_random_bananas(bananas)

    return jsonify(drawings=drawings)
