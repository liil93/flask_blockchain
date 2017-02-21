import requests, json

def login():
    url = url = 'http://127.0.0.1:7050/registrar'
    payload = {
	  'enrollId': 'admin',
	  'enrollSecret': 'Xurw3yU9zI0l'
	}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    return r.text
