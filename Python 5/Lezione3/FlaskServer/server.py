from flask import Flask, render_template, request
import json
import os.path
import datetime
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
@api.route('/login', methods=['GET'])
def login():
    with open('data/vittime.json') as f:
        vittime:dict = json.load(f)
    nome = request.args.get("Nome")
    print(f"Nome selezionato: {nome}")
    cognome = request.args.get("Cognome")
    print(f"Cognome selezionato: {cognome}")
    paprika = request.args.get("Paprika")
    print(f"Patatine {paprika} paprika")
    context = {
        "nome":nome, 
        "cognome":cognome,
        "paprika":paprika
        }
    for ki, vi in vittime.items():
    #if already a user
        last_pk:int = int(ki)
        if vi[0] == nome and vi[1] == cognome and vi[2] == paprika:
            return render_template('regko.html', **context)
    
    #if not a user
    vittime[str(last_pk+1)] = [nome, cognome, paprika]
    with open('data/vittime.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(vittime, indent=True))
    return render_template('regok.html', **context)


#preghiere
@api.route('/preghiere', methods=['GET'])
def preghiere():
    if os.path.exists('data/vittime.json'):
        return render_template('preghiere.html')
    else:
        raise Exception('The file "preghiere.json" has to be present in "data/" for the server to function!')

@api.route('/new_preghiera', methods=['POST'])
def new_preghiera():
    if request.method == 'POST':
        titolo_preg = request.form['titolo_preg']
        testo_preg = request.form['testo_preg']
        istante_preg = datetime.datetime.now()
    else:
        return render_template('preghiere.html')


@api.route('/lista_preghiere', methods=['GET'])
def lista_preghiere():
    pass


#api run segment
api.run(host="0.0.0.0", port=8085)