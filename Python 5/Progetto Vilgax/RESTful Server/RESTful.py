from flask import Flask, json, request, redirect, abort, jsonify
import os.path
import os
import psycopg2
from datetime import date
import json

api = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user=os.environ['postgres'],
            password=os.environ['postgres']
            )
    return conn

def table_fetch(reqtab:str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f'SELECT * FROM {reqtab};')
    table = cur.fetchall()
    cur.close()
    conn.close()
    return table

def table_mod(reqtab:str, new_data:str):
    pass



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
            with open(f'data/{data_name}.json', mode='w', encoding='utf-8') as f:
                json.dump(redata, f, indent=True)
            with open(f'data/{data_name}.json', mode='r') as f:
                sendata:dict = json.load(f)
            return jsonify(sendata)
        case _:
            abort(422)

if __name__ == '__main__'and\
os.path.exists('data/vittime.json') and\
os.path.exists('data/preghiere.json') and\
os.path.exists('data/recensioni.json'):
    api.run(host="127.0.0.1", port=1240, ssl_context='adhoc')