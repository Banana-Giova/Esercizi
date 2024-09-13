from flask import Flask, render_template, request
api = Flask(__name__, static_url_path='/static')

vittime:list[tuple[str]] = [
    ("Michelone", "Badasium"),
    ("Danielone", "Pietrosmusi"),
    ("Romeo", "Sgarrapisi"),
    ("Samuele", "Sgarrapisi"),
    ("Cristiano", "Ronaldo")
]

#main route
@api.route('/', methods=['GET'])
def vilgax():
    return render_template('vilgax.html')


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
    nome = request.args.get("Nome")
    print(f"Nome selezionato: {nome}")
    cognome = request.args.get("Cognome")
    print(f"Cognome selezionato: {cognome}")
    for i in vittime:
        if i[0] == nome and i[1] == cognome:
            return render_template('regko.html')
    return render_template('regok.html')


#api run segment
api.run(host="0.0.0.0", port=8085)