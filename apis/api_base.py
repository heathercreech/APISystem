import sys
import inspect

def all(module_name):
    api_endpoints = inspect.getmembers(sys.modules[module_name], inspect.isfunction)
    all_data = {}
    for entry in api_endpoints:
        if entry[0] != 'all':
            all_data.update({entry[0]: entry[1]()})
    return all_data