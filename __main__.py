import os
import sys
import json

from flask import Flask, request, url_for, jsonify

import auto_api


app = Flask(__name__)

def report_error(err_msg):
    return jsonify({'Error': err_msg})

#list all APIs
@app.route('/')
def directory_request():
    return jsonify({'apis': [api.split('.')[1] for api in auto_api.api_list]})

#list the endpoints associated to a specific API
@app.route('/<api_name>/')    
def api_directory_request(api_name=None):
    api_name = 'apis.' + api_name
    if api_name in auto_api.api_list:
        endpoint_names = list(auto_api.api_functions[api_name].keys())
        endpoint_names.sort()
        return jsonify({api_name: endpoint_names})
    else:
        return report_error('\'{0}\' is not a supported API'.format(api_name.split('.')[1])), 404
    
@app.route('/<api_name>/<api_func>/')
def endpoint_request(api_name=None, api_func=None):
    api_name = 'apis.' + api_name
    if api_name in auto_api.api_list:
        if api_func in auto_api.api_functions[api_name]:
            return jsonify(auto_api.call_api(api_name, api_func))
        else:
            return report_error('\'{0}\' is not an endpoint within the \'{1}\' api'.format(api_func, api_name.split('.')[1])), 404
    else:
        return report_error('\'{0}\' is not a supported API'.format(api_name.split('.')[1])), 404
    
if __name__ == '__main__':
    app.run(debug=False, port=5001)
