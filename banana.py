import json

FILE_PATH = 'banana.ndjson'

def gen_bananas():
    """ Create generator for ndjson file """
    for row in open(FILE_PATH, "r"):
        yield row

def get_bananas(gen):
    """ Grab 50 bananas from ndjson and extract drawing """
    data = []
    for i in range(50):
        try:
            line = next(gen)
            data.append(json.loads(line))
        except StopIteration:
            gen = gen_bananas(FILE_PATH)
    return [ image['drawing'] for image in data ]
