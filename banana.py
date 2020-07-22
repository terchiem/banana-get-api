import ndjson
import random

def load_bananas(filepath):
    """ Load drawings from ndjson file and return as list """
    print('loading bananas!')
    with open(filepath) as f:
        data = ndjson.load(f)
        return [ image['drawing'] for image in data ]

def get_random_bananas(bananas):
    """ Returns a new list of 50 random drawings """
    return random.sample(bananas, 50)