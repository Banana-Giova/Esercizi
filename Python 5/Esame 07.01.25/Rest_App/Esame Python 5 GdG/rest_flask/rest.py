from flask import Flask, json, request, redirect, abort, jsonify
import os
import psycopg2
import random
import string

def id_generator():
    caratteri = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(caratteri) for _ in range(12))
    return random_string

api = Flask(__name__)
db_tables:set = {
             'Case_in_vendita', 'Case_in_affitto', 
             'Filiali', 'Vendite_casa', 'Affitti_casa'
}

def get_db_connection():
    conn = psycopg2.connect(
            host="localhost",            #da cambiare ogni volta
            database='Immobiliare',      #con "ip addr show"
            user='postgres',             #172.21.24.242
            password='postgres',
            port='5432'
            )
    conn.autocommit = True
    return conn

def table_fetch(req_table:list):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT * FROM {req_table};')
            table = cur.fetchall()
    return table

@api.route('/', methods=['GET', 'POST'])
def index():
    redata = request.json.get('context', 0)
    print(f"\n\n{redata}\n\n")
    sOper:int = redata['operation']
    with open('data/curr_filiale.txt', mode='r') as reader:
        curr_filiale = reader.read()
    with open('data/curr_user.txt', mode='r') as reader:
        curr_user = reader.read()

    match int(sOper):
        case 0:
            filiale = redata['filiale']
            try:
                check = table_fetch(req_table=f"Filiali WHERE partita_iva ='{filiale}'")
                print(check)
                if len(check) == 0:
                    raise Exception("Nessuna filiale con tale partita IVA.")
                filiale_presente:bool = True
                curr_filiale = redata['filiale']
                with open('data/curr_filiale.txt', mode='w') as writer:
                    writer.write(curr_filiale)
            except Exception:
                filiale_presente = False
            output = {'filiale_presente':filiale_presente}
        case 1:
            new_query = redata['new_query']
            interrogation:str = f"Case_in_vendita WHERE metri >= {new_query['metri_min']} AND metri <= {new_query['metri_max']} AND vani >= {new_query['vani_min']} AND vani <= {new_query['vani_max']} AND prezzo >= {new_query['prezzo_min']} AND prezzo <= {new_query['prezzo_max']} AND stato = '{new_query['stato']}' AND venduta = FALSE"
            output = table_fetch(req_table=interrogation)
        case 2:
            new_query = redata['new_query']
            interrogation:str = f"Case_in_affitto WHERE tipo_affitto = '{new_query['tipo']}' AND bagno_personale = {new_query['bagno']} AND prezzo_mensile >= {new_query['prezzo_min']} AND prezzo_mensile <= {new_query['prezzo_max']} AND affittata = FALSE"
            print(interrogation)
            output = table_fetch(req_table=interrogation)
        case 3:
            new_query = redata['new_query']
            for ki, vi in new_query.items():
                if isinstance(vi, str):
                    new_query[ki] = vi.replace("'", "''")
            try:
                query:str = f"INSERT INTO Case_in_vendita (catastale, id, indirizzo, civico, piano, metri, vani, prezzo, stato, filiale_proponente, venduta)\nVALUES\n"
                query += f"('{new_query['catastale']}','{id_generator()}','{new_query['indirizzo']}',{new_query['civico']},{new_query['piano']},{new_query['metri']},{new_query['vani']},{new_query['prezzo']},'{new_query['stato']}','{curr_filiale}', FALSE);"
                print(query)
                with get_db_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(query=query)
                output = {'messa_in_vendita':True}
            except Exception as e:
                print(e)
                output = {'messa_in_vendita':False}    
        case 4:
            new_query = redata['new_query']
            for ki, vi in new_query.items():
                if isinstance(vi, str):
                    new_query[ki] = vi.replace("'", "''")
            try:
                query:str = f"INSERT INTO Case_in_affitto (catastale, id, indirizzo, civico, tipo_affitto, bagno_personale, prezzo_mensile, filiale_proponente, affittata)\nVALUES\n"
                query += f"('{new_query['catastale']}','{id_generator()}','{new_query['indirizzo']}','{new_query['civico']}','{new_query['tipo_affitto']}',{new_query['bagno']},{new_query['prezzo_mensile']},'{curr_filiale}', FALSE);"
                print(query)
                with get_db_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(query=query)
                output = {'messa_in_vendita':True}
            except Exception as e:
                print(e)
                output = {'messa_in_vendita':False}
        case 5:
            new_query = redata['new_query']
            for ki, vi in new_query.items():
                if isinstance(vi, str):
                    new_query[ki] = vi.replace("'", "''")
            try:
                check = table_fetch(req_table=f"Case_in_vendita WHERE id = '{new_query['id_select']}'")
                if len(check) == 0:
                    raise Exception("Nessuna casa in vendita con tale id presente.")
                acq_query:str = f"INSERT INTO Vendite_casa (catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita, acquirente)\nVALUES\n"
                acq_query += f"('{check[0][0]}',CURRENT_DATE,'{check[0][9]}','{curr_filiale}',{new_query['prezzo_vendita']},'{curr_user}');"
                up_query:str = f"UPDATE Case_in_vendita SET venduta = TRUE WHERE id='{new_query['id_select']}';"
                with get_db_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(query=acq_query)
                        cur.execute(query=up_query)
                acquisto_completato = True
            except Exception as e:
                print(e)
                acquisto_completato = False
            output = {'acquisto_completato':acquisto_completato}
        case 6:
            new_query = redata['new_query']
            for ki, vi in new_query.items():
                if isinstance(vi, str):
                    new_query[ki] = vi.replace("'", "''")
            try:
                check = table_fetch(req_table=f"Case_in_affitto WHERE id = '{new_query['id_select']}'")
                if len(check) == 0:
                    raise Exception("Nessuna casa in affitto con tale id presente.")
                acq_query:str = f"INSERT INTO Affitti_casa (catastale, data_affitto, filiale_proponente, filiale_venditrice, prezzo_affitto, durata_contratto, acquirente)\nVALUES\n"
                acq_query += f"('{check[0][0]}',CURRENT_DATE,'{check[0][7]}','{curr_filiale}',{new_query['prezzo_affitto']},'{new_query['durata_contratto']}','{curr_user}');"
                up_query:str = f"UPDATE Case_in_affitto SET affittata = TRUE WHERE id='{new_query['id_select']}';"
                with get_db_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(query=acq_query)
                        cur.execute(query=up_query)
                acquisto_completato = True
            except Exception as e:
                print(e)
                acquisto_completato = False
            output = {'acquisto_completato':acquisto_completato}
        case 7:
            new_query = redata['new_query']
            for ki, vi in new_query.items():
                if isinstance(vi, str):
                    new_query[ki] = vi.replace("'", "''")
                check = table_fetch(req_table=f"Utenti WHERE username = '{new_query['username']}'")
                if len(check) == 0:
                    query:str = f"INSERT INTO Utenti (username, password)\nVALUES\n"
                    query += f"('{new_query['username']}', '{new_query['password']}');"
                    print(query)
                    with get_db_connection() as conn:
                        with conn.cursor() as cur:
                            cur.execute(query=query)
                    utente_nuovo = True
                    password_errata = False
                    with open('data/curr_user.txt', mode='w') as writer:
                        writer.write(new_query['username'])
                else:
                    utente_nuovo = False
                    check = table_fetch(req_table=f"Utenti WHERE username = '{new_query['username']}' AND password = '{new_query['password']}'")
                    if len(check) == 0:
                        password_errata = True
                    else:
                        password_errata = False
                        with open('data/curr_user.txt', mode='w') as writer:
                            writer.write(new_query['username'])
            output = {'utente_nuovo':utente_nuovo, 'password_errata':password_errata}
        case _:
            abort(422)

    return jsonify(output)



if __name__ == '__main__':
    api.run(host="0.0.0.0", port=4160)