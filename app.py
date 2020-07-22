from flask import Flask, jsonify
from banana import load_bananas, get_random_bananas

bananas = load_bananas('banana.ndjson')

app = Flask(__name__)

@app.route('/')
def get_bananas():
    """ Returns 50 bananas """

    drawings = get_random_bananas(bananas)

    return jsonify(drawings=drawings)

