__author__ = 'AleLore'

import json

def save_json(filename, data):
    with open('{0}.json'.format(filename),'w') as f:
        json.dump(data, f)



def load_json(filename):
    with open('{0}.json'.format(filename))as f:
        data = json.load(f)
    return data

def load_huge_jsonFile(filename):
    with open('{0}.json'.format(filename), 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
            except:
                print('Error 1 ')
                break
    return data