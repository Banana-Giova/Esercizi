from flask import Flask, json, request, redirect # type: ignore
import os.path
from datetime import date
import json
import ast

api = Flask(__name__)

valid_nums = [1,2,3,4,5,6,7]

@api.route('/', methods=['GET', 'POST'])
def restful_get():
    if request.method == 'POST':
        sOper = int(request.form['test'])
    if sOper not in valid_nums:
        raise Exception("Operazione non valida.")    
    while sOper != 7:
        if sOper == 1:
            with open('data/vittime.json', mode='r') as f:
                vittime:dict = json.load(f)
                return vittime
        elif sOper == 2:
            with open('data/preghiere.json', mode='r') as f:
                preghiere:dict = json.load(f)
                return preghiere
        elif sOper == 3:
            with open('data/recensioni.json', mode='r') as f:
                recensioni:dict = json.load(f)
                return recensioni
        else:
            return redirect(f'/mod{sOper}')
        
@api.route('/mod4', methods=['GET'])
def restful_mod4():
    try:
        vittime = ast.literal_eval(input("Fornire nuovo dizionario\n>>>"))
        with open('data/vittime.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(vittime, indent=True))
        return "Successo"
    except:
        return "Fallimento"

@api.route('/mod5', methods=['GET'])
def restful_mod5():
    try:
        preghiere = ast.literal_eval(input("Fornire nuovo dizionario\n>>>"))
        with open('data/preghiere.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(preghiere, indent=True))
        return "Successo"
    except:
        return "Fallimento"

@api.route('/mod6', methods=['GET'])
def restful_mod6():
    try:
        recensioni = ast.literal_eval(input("Fornire nuovo dizionario\n>>>"))
        with open('data/recensioni.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(recensioni, indent=True))
        return "Successo"
    except:
        return "Fallimento"

if __name__ == '__main__'and\
os.path.exists('data/vittime.json') and\
os.path.exists('data/preghiere.json') and\
os.path.exists('data/recensioni.json'):
    api.run(host="127.0.0.1", port=1240)