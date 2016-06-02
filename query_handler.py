import sys

import apis.about


def list_apis():
    modules = [key for key in sys.modules.keys() if 'apis' in key and key != 'apis']
    api_list = []
    for entry in modules:
        api_list.append(entry)
    return api_list

def list_functions(module):
    module_functions = [func_name for func_name in dir(module) if "__" not in func_name]
    return module_functions
    
    
api_list = list_apis()
api_functions = []
for api in api_list:
    api_functions.append(list_functions(sys.modules[api]))
print(api_functions)
    
def api_call():
    print(dir(apis.about))