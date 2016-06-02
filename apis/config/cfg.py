from . import yaml_fio as yfio

file_format = '.yaml'

def relative_fn(file_name):
    split_fn = file_name.split('.')
    mod_fn = ''
    for i in range(0, len(split_fn)-1):
        mod_fn += split_fn[0] + '/'
    mod_fn += "config/" + split_fn[-1]
    return mod_fn

def load_file(file_name):
    file_name = relative_fn(file_name)
    return yfio.load_file(file_name + file_format)

def save_file(file_name, data):
    file_name = relative_fn(file_name)
    return yfio.save_data(file_name + file_format, data)