from . import yaml_fio as yfio
from . import json_fio as jfio

file_format = '.yaml'

def relative_fn(file_name):
    split_fn = file_name.split('.')
    mod_fn = ''
    for i in range(0, len(split_fn)-1):
        mod_fn += split_fn[0] + '/'
    mod_fn += 'config/' + split_fn[-1]
    return mod_fn

def format_to_module(file_format):
    if file_format == 'json':
        return jfio
    if file_format == 'yaml':
        return yfio
    else:
        raise Exception('Supplied file format is not supported')

def load_file(file_name, file_format='json'):
    file_name = relative_fn(file_name)
    fio_module = format_to_module(file_format)
    return yfio.load_file(file_name + '.' + file_format)

def save_file(file_name, data, file_format='json'):
    file_name = relative_fn(file_name)
    fio_module = format_to_module(file_format)
    return fio_module.save_data(file_name + '.' + file_format, data)