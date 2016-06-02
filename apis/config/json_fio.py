import json

def load_file(filename):
    return json.load(filename)
    
def save_file(filename, data):
    return json.dump(filename, data)