from flask import Flask, render_template, request, jsonify
from numpy import int8
from flask_cors import CORS
import requests
import json
from datetime import date

app = Flask(__name__)
CORS(app,support_credentials = True)

@app.route('/')


@app.route('/getnews')
def getFeed():
    
    interests = request.args.get('interests', 0, type=str)
    n = request.args.get('n', 0, type=int8)

    print(interests)
    print(n)

    today = date.today()
    month = (today.month - 1)
    day = today.day + 1
    d = today.replace(day = day, month = month)
    d = str(d)
    
    API_KEY = 'dc7fb1d2a4c44ceabd4173d71cacb27a'

    results = []
    for query in interests.split(','):
        
        url = ('https://newsapi.org/v2/everything?'
            'q='+ query+'&'
            'from='+d+'&' ##need to change based on current date
            'sortBy=popularity&'
            'language=en&'
            'apiKey='+API_KEY)

        response = requests.get(url)
        r = response.json()
        if(r['totalResults'] > 0):
            res = r['articles'][0:n]
            for ele in res:
                results.append(ele)

    results.sort(key=lambda x: x["publishedAt"])

    print(results)

    with open("newsJson.json", "a") as o:
        o.write(results)

if __name__ == "__main__":
    app.run()