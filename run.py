#!flask/bin/python
from app import app
from app import chaincode

a = chaincode.login()
print(a)

app.run(debug=True)
