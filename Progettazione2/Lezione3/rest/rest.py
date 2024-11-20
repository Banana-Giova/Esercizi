from flask import Flask, g, json, request, redirect, abort, jsonify
import os
import psycopg2
from datetime import date

def cojostarter():
    with open('cojocounter.txt', mode='w') as coca:
        coca.write('0')
cojostarter()

def cojoadder():
    with open('cojocounter.txt', mode='r') as coca:
        recoca = int(coca.read())
    with open('cojocounter.txt', mode='w') as coca:
        coca.write(f'{recoca+1}')
    return recoca+1

api = Flask(__name__)
db_tables = {
    'Cielo':('Aeroporto', 'ArrPart', 'LuogoAeropoto',
             'Volo', 'Compagnia'),

    'Accademia': ('Persona', 'Progetto',
                 'AttivitaNonProgettuale', 
                 'AttivitaProgetto', 
                 'WP', 'Assenza')
}

insulti_costruttivi = {
    1:'La tabella selezionata non esiste, si prega di inserirne una valida.',
    2:'Per piacere inserire una tabella valida.',
    3:'Inserisci una tabella valida!',
    4:'Hai rotto i c******i, inserisci una tabella valida o crasho il server.'
}

def get_db_connection(database:str):
    conn = psycopg2.connect(
            host="localhost",
            database=database,
            user='postgres',
            password='postgres',
            port='5432'
            )
    conn.autocommit = True
    return conn

def table_fetch(req_database:str, req_table:list):
    with get_db_connection(database=req_database) as conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT * FROM {req_table};')
            table = cur.fetchall()
    return table

@api.route('/', methods=['GET', 'POST'])
def index():
    redata = request.json.get('context', 0)
    print(f"\n\n{redata}\n\n")
    req_db = redata['req_db']

    match int(req_db):
        case 1:
            database_name = 'Accademia'
        case 2:
            database_name = 'Cielo'
        case _:
            abort(422)
    
    try:
        table_name = redata['req_tab']
        if table_name not in db_tables[database_name]:
            raise TypeError(f"{table_name} does not exist in this database!")

        sendata = table_fetch(req_database=database_name,
                              req_table=table_name)
    except Exception as e:
        cojocounter = cojoadder()
        if cojocounter   < 5:
            sendata = insulti_costruttivi[cojocounter]
        else:
            abort(422)
            
    return jsonify(sendata)



if __name__ == '__main__':
    api.run(host="127.0.0.1", port=7160, ssl_context='adhoc')