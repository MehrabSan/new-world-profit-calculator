import os
# import requests
import json

def delete_old_data_file(filename='download.json'):
    if os.path.exists(filename):
        os.remove(filename)

def download_data(server_id):
    """
    Offline stub: load local 'download.json' or return empty dict.
    """
    filename = 'download.json'
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    # no local file; return empty dict
    return {}

def save_data_to_file(data, filename='download.json'):
    delete_old_data_file(filename)  
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data_from_file(filename='download.json'):
    with open(filename, 'r') as f:
        return json.load(f)
