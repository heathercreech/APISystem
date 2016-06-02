import sys
import inspect

import apis
from apis import *


def list_apis():
    return ['apis.' + api_name for api_name in apis.__all__]

def list_functions(module):
    module_functions = inspect.getmembers(module, inspect.isfunction)
    mf_dict = {}
    for entry in module_functions:
        mf_dict.update({entry[0]: entry[1]})
    return mf_dict
    
api_list = list_apis()
api_functions = {}
for api in api_list:
    api_functions.update({api: list_functions(sys.modules[api])})
    
def call_api(api_name, api_func):
    return api_functions[api_name][api_func]()
