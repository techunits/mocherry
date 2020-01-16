import json
import os
import pprint

def load_config():
    settings_path = os.environ.get('MOCHERRY_SETTINGS_PATH')
    with open(settings_path, 'r') as fp:
        filedata = fp.read()
        return json.loads(filedata)

CONFIG = load_config()
CONFIG['basepath'] = os.getcwd()
