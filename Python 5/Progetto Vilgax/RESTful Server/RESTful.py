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
            user='postgres',
            password='postgres',
            port='5432'
            )
    conn.autocommit = True
    return conn

def table_fetch(reqtab:str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f'SELECT * FROM {reqtab};')
    table = cur.fetchall()
    cur.close()
    conn.close()
    return table

def table_mod(sOper:str, new_query:dict):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        match int(sOper):

            #vittime
            case 4:
                for ki, vi in new_query.items():
                    new_query[ki] = vi.replace("'", "''")
                query:str = f"INSERT INTO Vittime (id, nome, cognome, paprika)\nVALUES\n"
                query += f"('{new_query['id']}','{new_query['nome']}','{new_query['cognome']}','{new_query['paprika']}');"
                cur.execute(query=query)

            #preghiere
            case 5:
                if new_query != None:                
                    for ki, vi in new_query.items():
                        if ki != 'data':
                            new_query[ki] = vi.replace("'", "''")
                    query:str = f"INSERT INTO Preghiere (proprietario, titolo, contenuto, data)\nVALUES\n"
                    query += f"('{new_query['proprietario']}','{new_query['titolo']}','{new_query['contenuto']}','{new_query['data']}');"
                    cur.execute(query=query)

            #recensioni
            case 6:
                for ki, vi in new_query.items():
                    if not isinstance(vi, int):
                        new_query[ki] = vi.replace("'", "''")

                cur.execute(f"SELECT *\nFROM Recensioni\nWHERE proprietario = '{new_query['proprietario']}'")
                check = cur.fetchall()
                if len(check) != 0:
                    cur.execute(f"UPDATE Recensioni\nSET descrizione='{new_query['descrizione']}',voto='{new_query['voto']}'\nWHERE proprietario='{new_query['proprietario']}'")
                else:
                    query:str = f"INSERT INTO Recensioni (id, proprietario, descrizione, voto)\nVALUES\n"
                    query += f"('{new_query['id']}','{new_query['proprietario']}','{new_query['descrizione']}','{new_query['voto']}');"
                    cur.execute(query=query)
            
            #flusso di coscienza
            case 7:
                try:
                    cur.execute(f"{new_query}")
                    if 'SELECT' in new_query.upper():
                        outflux = cur.fetchall()
                    else:
                        outflux = "Query eseguita con successo"
                    output = {'elab_query': outflux}
                except Exception:
                    output = None
                finally:
                    cur.close()
                    conn.close()
                return output

            case _:
                raise ConnectionRefusedError
    except Exception as e:
        raise Exception(e)
    finally:
        cur.close()
        conn.close()


@api.route('/', methods=['GET', 'POST'])
def index():
    sOper = request.json.get('req_type', 0)

    match int(sOper):
        case 1 | 4:
            data_name = 'vittime'
        case 2 | 5:
            data_name = 'preghiere'
        case 3 | 6:
            data_name = 'recensioni'
        case 7:
            data_name = 'admin'
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
                json.dump(redata[data_name], f, indent=True)
            with open(f'data/{data_name}.json', mode='r') as f:
                sendata:dict = json.load(f)

            table_mod(sOper, redata['new_query'])
            return jsonify(sendata)
        
        case 7:
            redata = request.json.get('context', 0)
            sendata = table_mod(7, redata['new_query'])
            print(sendata)
            return jsonify(sendata)
        
        case _:
            abort(422)

if __name__ == '__main__'and\
os.path.exists('data/vittime.json') and\
os.path.exists('data/preghiere.json') and\
os.path.exists('data/recensioni.json'):
    api.run(host="127.0.0.1", port=1240, ssl_context='adhoc')