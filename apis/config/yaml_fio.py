import yaml

def load_file(file_name):
    with open(file_name, 'r') as yf:
        return yaml.load(yf)

def save_file(file_name, data):
    with open(file_name, 'w') as yf:
        yf.write(yaml.dump(data))