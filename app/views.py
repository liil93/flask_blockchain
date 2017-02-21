from flask import render_template, flash, redirect, request, Response
from app import app
import json, requests



#test
@app.route('/test', methods=['GET'])
def test():
	data = {"type": "text"}
	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')
	return resp


# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/keyboard', methods=['GET'])
def keyboard():
	data = {"type": "text"}
	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')
	return resp

#친구 추가 알림 API
@app.route('/friend', methods=['POST'])
def friend_add():
	resp = Response('SUCCESS', status=200, mimetype='application/json')
	return resp

#친구 차단 알림 API
@app.route('/friend/<user_key>', methods=['DELETE'])
def friend_delete(user_key):
	resp = Response('SUCCESS', status=200, mimetype='application/json')
	return resp


#채팅방 나가기
@app.route('/chat_room/<user_key>', methods=['DELETE'])
def chat_room_exit(user_key):
	resp = Response('SUCCESS', status=200, mimetype='application/json')
	return resp

#채팅방 나가기
@app.route('/login', methods=['GET'])
def login():
    url = url = 'http://127.0.0.1:7050/registrar'
    payload = {
	  'enrollId': 'admin',
	  'enrollSecret': 'Xurw3yU9zI0l'
	}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp

#채팅방 나가기
@app.route('/init', methods=['GET'])
def deploy():
    url = url = 'http://127.0.0.1:7050/chaincode'
    payload = {
        "jsonrpc": "2.0",
        "method": "deploy",
        "params": {
            "type": 1,
            "chaincodeID":{
                "name": "mycc"
            },
            "ctorMsg": {
                "args":[""]
            },
            "secureContext": "admin"
        },
        "id": 1
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    js = json.loads(r.text)
    js = json.dumps(js)

    resp = Response(js, status=200, mimetype='application/json')
    return resp


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

# @app.route('/message', methods=['GET', 'POST'])
# def message():
#     data_decode = request.data.decode()
#     data_loads = json.loads(data_decode)
#     print(data_decode)
#
#     user_db = read_user_db(data_loads)
#     user_step = user_db[0]
#     user_movie = user_db[1]
#
#     print(user_step)
#
#     #0000 --> 처음 영화 입력
#     #0001 --> 영화 간단 소개 받음.
#     #0010 --> 영화 상세 소개 받음.
#     if user_step == '0000':
#     	flag, list_movie = CompareMovie(data_loads['content'])
#     	message = flag_movie(data_loads, flag, list_movie)
#     elif user_step == '0001':
#         content = data_loads['content']
#         content = content.split('.')
#         if content[0] == '1':  #상세정보
#             message = detail_movie(user_movie)
#             change_user_DB(data_loads, '0010', user_movie)
#         elif content[0] == '2':    #비슷한 영화
#             message = sims(data_loads, user_movie)
#         elif content[0] == '3':     #주변 극장
#             message = yet_pass(data_loads)
#         elif content[0] == '0':    #취소
#             message = cancel(data_loads)
#         else:
#             message = error(data_loads)
#
#     elif user_step == '0010':
#         content = data_loads['content']
#         content = content.split('.')
#         if content[0] == '1':   #비슷한 영화
#             message = sims(data_loads, user_movie)
#         elif content[0] == '2': #주변 극장
#             message = yet_pass(data_loads)
#         elif content[0] == '0': #취소
#             message = cancel(data_loads)
#         else:
#             message = error(data_loads)
#     else:
#     	message = error(data_loads)
#
#
#     data_result = message
#     js = json.dumps(data_result)
#     resp = Response(js, status=200, mimetype='application/json')
#       #resp.headers['Text'] = 'fuck'
#     return resp
