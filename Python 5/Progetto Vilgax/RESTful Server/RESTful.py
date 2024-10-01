from flask import Flask, json, request, redirect, abort, jsonify
import os.path
from datetime import date
import json

api = Flask(__name__)

@api.route('/', methods=['GET', 'POST'])
def index():
    sOper = request.json.get('test', 0)
    match int(sOper):
        case 1 | 4:
            data_name = 'vittime'
        case 2 | 5:
            data_name = 'preghiere'
        case 3 | 6:
            data_name = 'recensioni'
        case _:
            abort(422)
    match int(sOper):
        case 1 | 2 | 3:
            with open(f'data/{data_name}.json', mode='r') as f:
                sendata:dict = json.load(f)
                return jsonify(sendata)
        case 4 | 5 | 6:
            redata = request.json.get('context', 0)
            with open(f'data/{data_name}.json', mode='a', encoding='utf-8') as f:
                f.write(json.dumps(redata, indent=True))
            with open(f'data/{data_name}.json', mode='r') as f:
                sendata:dict = json.load(f)
            return jsonify(sendata)
        case _:
            abort(422)

if __name__ == '__main__'and\
os.path.exists('data/vittime.json') and\
os.path.exists('data/preghiere.json') and\
os.path.exists('data/recensioni.json'):
    api.run(host="127.0.0.1", port=1240)