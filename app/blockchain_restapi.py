from flask import render_template, flash, redirect, request, Response
from app import app
import json, requests

def login():
    try:
        url = url = 'http://127.0.0.1:7050/registrar'
        payload = {
    	  'enrollId': 'admin',
    	  'enrollSecret': 'Xurw3yU9zI0l'
    	}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        return r.text
    except:
        return "Chaincode is not working."

        
#INVOKE
@app.route('/insert', methods=['GET'])
def insert():
    url = url = 'http://127.0.0.1:7050/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "invoke",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["pet_insert", "01050054471", "DDONG", "4", "female", "dog", "3", "1", "1", "sdlfkjklsdfjlksdjflksf"]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#Qeury
@app.route('/read', methods=['GET'])
def read():
    url = url = 'http://127.0.0.1:7050/chaincode'
    payload = {
      "jsonrpc": "2.0",
      "method": "query",
      "params": {
          "type": 1,
          "chaincodeID":{
              "name":"mycc"
          },
          "ctorMsg": {
             "args":["pet_read","01050054471"]
          },
          "secureContext": "admin"
      },
      "id": 3
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp
