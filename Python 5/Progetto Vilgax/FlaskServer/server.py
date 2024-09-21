from flask import Flask, render_template, request, redirect
import json
from models import Preghiera
import os.path
from datetime import date
api = Flask(__name__, static_url_path='/static')


#main route
@api.route('/', methods=['GET'])
def vilgax():
    if os.path.exists('data/vittime.json'):
        return render_template('vilgax.html')
    else:
        raise Exception('The file "vittime.json" has to be present in "data/" for the server to function!')


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


#registration
@api.route('/login', methods=['POST'])
def login():
    with open('data/vittime.json') as f:
        vittime:dict = json.load(f)
    if request.method == "POST":
        nome = request.form["Nome"]
        print(f"Nome selezionato: {nome}")
        cognome = request.form["Cognome"]
        print(f"Cognome selezionato: {cognome}")
        paprika = request.form["Paprika"]
        print(f"Patatine {paprika} paprika")
    else:
        return render_template('vilgax.html')
    context = {
        "nome":nome, 
        "cognome":cognome,
        "paprika":paprika
        }
    for ki, vi in vittime.items():
    #if already a user
        last_pk:int = int(ki)
        if vi[0] == nome and vi[1] == cognome and vi[2] == paprika:
            if paprika == 'senza':
                papritext:str = 'S'
            elif paprika == 'con':
                papritext = 'C'
            global current_user
            current_user = nome + cognome + papritext
            global current_day
            current_day = int((str(date.today())).replace('-',''))
            return render_template('regko.html', **context)
    
    #if not a user
    vittime[str(last_pk+1)] = [nome, cognome, paprika]
    with open('data/vittime.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(vittime, indent=True))
    return render_template('regok.html', **context)


#preghiere
@api.route('/preghiere', methods=['GET'])
def preghiere():
    if os.path.exists('data/preghiere.json'):
        with open('data/preghiere.json', mode='r') as f:
            preghiere:dict = json.load(f)
        if current_user not in preghiere:
            preghiere[current_user] = []
        with open('data/preghiere.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(preghiere, indent=True))

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
    else:
        raise Exception('The file "preghiere.json" has to be present in "data/" for the server to function!')

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
    with open('data/preghiere.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(preghiere, indent=True))
    return redirect('/preghiere')


#api run segment
api.run(host="0.0.0.0", port=8085)