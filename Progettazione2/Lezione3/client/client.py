from flask import Flask, render_template, request, redirect # type: ignore
import json
import requests
from datetime import date
api = Flask(__name__, static_url_path='/static')

def fetchOrMoni(context:dict={}) -> dict:
    try:
        data = { 'context': context }

        url = 'https://127.0.0.1:7160/'
        headers = { 'Content-Type': 'application/json' }
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
        response.raise_for_status()
        #data = json.load((response.json()))
        output = response.json()

        return output
    except Exception as e:
        raise Exception(f"Error during Fetch Or Moni:\n{e}")

"""@api.route('/', methods=['GET', 'POST'])
def index():
    render_template('index.html')"""

@api.route('/', methods=['GET'])
def toni_mancini():
    context = {
        'requested': False,
        'type': None,
        'query_torno': None
    }
    return render_template('moni_tancini.html', **context)

@api.route('/moni_tancini', methods=['POST'])
def moni_tancini():
    if request.method == "POST":
        req_db = request.form["req_db"]
        req_tab = request.form["req_tab"]
    else:
        return render_template('moni_tancini.html')
    post_it = {
        'req_db':req_db,
        'req_tab':req_tab
    }

    query_torno = fetchOrMoni(post_it)
    #print(f"\n\n{isinstance(query_torno, str)}\n\n")
    
    if isinstance(query_torno, str):
        query_type = 'string'
    elif isinstance(query_torno, list):
        query_type = 'list'
    else:
        raise TypeError("The REST Server returned an invalid type.")

    context = {
        'requested': True,
        'type': query_type,
        'query_torno': query_torno
    }
    return render_template('moni_tancini.html', **context)



#api run segment
if __name__ == '__main__':
    api.run(host="127.0.0.1", port=6071, ssl_context='adhoc')