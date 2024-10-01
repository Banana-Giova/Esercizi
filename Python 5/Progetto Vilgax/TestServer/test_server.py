from flask import Flask, json, redirect # type: ignore
import json
import requests

api = Flask(__name__)

@api.route('/', methods=['GET'])
def testing():
    data = { 'test': 4 }
    addict:dict = {"1": 
                  ["Pippo", "Baudo", "senza"]}
    
    url = 'http://127.0.0.1:1240/'
    headers = { 'Content-Type': 'application/json' }
    response = requests.post(url, data=json.dumps(data), headers=headers,
                             json=addict)
    response.raise_for_status()
    data = response.json()
    
    return data


if __name__ == '__main__':
    api.run(host="127.0.0.1", port=2480)