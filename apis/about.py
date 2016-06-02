import sys
import inspect

from .config import cfg
from . import api_base

about_data = cfg.load_file(__name__, file_format='yaml')

def all():
    return api_base.all(__name__)

def basic():
    return {'name': about_data['name']}
    
def contact():
    return {'email': about_data['email']}
    
def portfolio():
    return {'github': about_data['github'], 'website': about_data['website']}
