from flask import Flask, render_template, request, redirect # type: ignore
import json
import requests
from models import Preghiera
from datetime import date
api = Flask(__name__, static_url_path='/static')

#to fetch or mod a specific json
def fetchOrMod(fetch_num:int, context:dict={}) -> dict:
    try:
        data = { 'req_type': fetch_num,
                 'context': context }

        url = 'https://127.0.0.1:1240/'
        headers = { 'Content-Type': 'application/json' }
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
        response.raise_for_status()
        #data = json.load((response.json()))
        output = response.json()

        return output
    except Exception as e:
        raise Exception(f"Error during Fetch Or Mod:\n{e}")


#to fetch all jsons
def fetchAll():
    try:
        vittime = fetchOrMod(1)
        with open('data/vittime.json', mode='w', encoding='utf-8') as f:
            json.dump(vittime, f, indent=True)
        preghiere = fetchOrMod(2)
        with open('data/preghiere.json', mode='w', encoding='utf-8') as f:
            json.dump(preghiere, f, indent=True)
        recensioni = fetchOrMod(3)
        with open('data/recensioni.json', mode='w', encoding='utf-8') as f:
            json.dump(recensioni, f, indent=True)
    except Exception as e:
        raise Exception(f"Error during Fetch All:\n{e}")


#main route
@api.route('/', methods=['GET'])
def vilgax():
    fetchAll()
    return render_template('vilgax.html')

#session daemon
def session_daemon(n:str, c:str, p:str):
    if p == 'senza':
        papritext:str = 'S'
    elif p == 'con':
        papritext = 'C'
    
    global current_nome
    current_nome = n
    global current_cognome
    current_cognome = c
    global current_paprika
    current_paprika = p
    global current_user
    current_user = n + c + papritext

    global current_day
    current_day = int((str(date.today())).replace('-',''))

#secondary routes
@api.route('/michelone', methods=['GET'])
def michelone():
    return render_template('2nd_routes/michelone.html')
@api.route('/danielone', methods=['GET'])
def danielone():
    return render_template('2nd_routes/danielone.html')
@api.route('/romeo', methods=['GET'])
def romeo():
    return render_template('2nd_routes/romeo.html')
@api.route('/samuele', methods=['GET'])
def samuele():
    return render_template('2nd_routes/samuele.html')
@api.route('/ronaldo', methods=['GET'])
def ronaldo():
    return render_template('2nd_routes/ronaldo.html')
@api.route('/alt_ko', methods=['GET'])
def review_ko():
    context = {
        "nome":current_nome, 
        "cognome":current_cognome,
        "paprika":current_paprika
        }
    return render_template('regko.html', **context)

@api.route('/review_search')
def review_search():
    context = {
        'searched': False,
        'recensione': None
    }
    return render_template('review_search.html', **context)

#registration
@api.route('/login', methods=['POST'])
def login():
    with open('data/vittime.json') as f:
        vittime:dict = json.load(f)
    if request.method == "POST":
        nome = request.form["Nome"]
        cognome = request.form["Cognome"]
        paprika = request.form["Paprika"]
    else:
        return render_template('vilgax.html')
    context = {
        "nome":nome, 
        "cognome":cognome,
        "paprika":paprika
        }
    
    session_daemon(n=nome, c=cognome, p=paprika)
    for ki, vi in vittime.items():
    #if already a user
        if vi[0] == nome and vi[1] == cognome and vi[2] == paprika:
            return render_template('regko.html', **context)
    
    #if not a user
    context["id"] = current_user
    vittime[current_user] = [nome, cognome, paprika]
    mod_context = {
        'vittime':vittime,
        'new_query':context
    }
    
    fetched = fetchOrMod(4, mod_context)
    with open('data/vittime.json', mode='w', encoding='utf-8') as f:
        json.dump(fetched, f, indent=True)
    return render_template('regok.html', **context)

@api.route('/get_info', methods=['POST'])
def get_info():
    with open('data/recensioni.json') as f:
        recensioni:dict = json.load(f)
    if request.method == "POST":
        cf = request.form["CF"]
        text_review = request.form["text_review"]
        stars = request.form["star-input"]
    else:
        return render_template('vilgax.html')
    insert_recensione = {

    }

    updated:bool = False
    #if already made a review
    if cf in recensioni:
        updated = True
        del recensioni[cf]
        
    recensioni[cf] = [text_review, stars]
    context = {
        'updated': updated
    }
    fetch_context = {
        'recensioni':recensioni,
        'new_query':insert_recensione
    }

    fetched = fetchOrMod(6, recensioni)
    with open('data/recensioni.json', mode='w', encoding='utf-8') as f:
        json.dump(fetched, f, indent=True)
    return render_template('review_sent.html', **context)

#preghiere
@api.route('/preghiere', methods=['GET'])
def preghiere():
    with open('data/preghiere.json', mode='r') as f:
        preghiere:dict = json.load(f)
    if current_user not in preghiere:
        preghiere[current_user] = []
    fetched = fetchOrMod(5, preghiere)
    with open('data/preghiere.json', mode='w', encoding='utf-8') as f:
        json.dump(fetched, f, indent=True)

    current_preghiere:list[list[str, str, int]] = preghiere[current_user]
    context = {
        "da_esaudire": [],
        "esaudite": []
    }
    for i in current_preghiere:
        singola_preg = Preghiera(
            titolo=i[0], testo=i[1], data=i[2]
        )
        if singola_preg.data >= current_day:
            context["da_esaudire"].insert(0, singola_preg)
        else:
            context["esaudite"].insert(0, singola_preg)
    return render_template('preghiere.html', **context)

#new_preghiera
@api.route('/new_preghiera', methods=['POST'])
def new_preghiera():
    if request.method == 'POST':
        titolo_preg = request.form['titolo_preg']
        print(titolo_preg)
        testo_preg = request.form['testo_preg']
        print(testo_preg)
        istante_preg = int((str(date.today())).replace('-',''))
        print(istante_preg)
    else:
        return render_template('preghiere.html')
    preghierina:list = [titolo_preg, testo_preg, istante_preg]
    
    with open('data/preghiere.json', mode='r', encoding='utf-8') as f:
        preghiere:dict = json.load(f)
    if current_user not in preghiere:
        preghiere[current_user] = []
    preghiere[current_user].append(preghierina)
    fetched = fetchOrMod(5, preghiere)
    with open('data/preghiere.json', mode='w', encoding='utf-8') as f:
        json.dump(fetched, f, indent=True)
    return redirect('/preghiere')

#list_reviews
@api.route('/list_reviews', methods=['POST'])
def list_reviews():
    if request.method == 'POST':
        cf = request.form['CF']
        print(cf)
        with open('data/recensioni.json', mode='r') as f:
            recensioni:dict = json.load(f)

        if cf not in recensioni:
            recensione = None
            print("Non lo trovo!")
        else:
            recensione = recensioni[cf]
            print("Trovato!")

        context = {
            'searched': True,
            'recensione': recensione
            }
        return render_template('review_search.html', **context)
    else:
        return render_template('review_search.html')



#api run segment
if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8085, ssl_context='adhoc')