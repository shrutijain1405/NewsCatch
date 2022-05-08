from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from datetime import date

# Set up Flask:
app = Flask(__name__)

# Set up Flask to bypass CORS:
cors = CORS(app, support_credentials=True)

# Create the receiver API POST endpoint:


@app.route("/receiver1", methods=["POST"])
def postME():
    logininfo = request.get_json()
    n = 20

    usrname = logininfo[0]['username']
    pwd = logininfo[0]['password']
    print(usrname)
    print(pwd)

    success = False

    suc = {"suc": 0, "interests": []}
    f = open('LoginSystemData.json', 'r')
    data = json.load(f)
    # print("hii")
    found = False
    for i in data:
        a = i['username']
        b = i['password']
        if(a == user and b == passwd):
            suc["suc"] = 1
            suc["interests"] = i['news']
            found = True
            break

    if(found == False):
        print("login not successful")
    f.close()

    data = jsonify(suc)
    print(suc)
    return data


if __name__ == "__main__":
    app.run(debug=True)
