from flask import Flask, json, redirect # type: ignore
import json
import socket, time
import requests

api = Flask(__name__)

context = {
    'test':1
}

@api.route('/', methods=['GET'])
def testing():
    response = requests.post("http://127.0.0.1:1240", data=context)
    return 

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=2480)