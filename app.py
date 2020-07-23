from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from banana import get_bananas, gen_bananas

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

gen = gen_bananas()

@app.route('/')
@cross_origin()
def get_drawings():
    drawings = get_bananas(gen)

    return jsonify(drawings=drawings)
