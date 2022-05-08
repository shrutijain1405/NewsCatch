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


@app.route("/receiver", methods=["POST"])
def postME():
    inter = request.get_json()
    n = 20

    interests = inter[0]['interests']
    print(interests)
    print(n)

    today = date.today()
    month = (today.month - 1)
    day = today.day + 1
    d = today.replace(day=day, month=month)
    d = str(d)

    API_KEY = '6c7f0343d64d48fead0da3b5dd3782de'

    results = []
    for query in interests.split(','):

        url = ('https://newsapi.org/v2/everything?'
               'q=' + query+'&'
               'from='+d+'&'  # need to change based on current date
               'sortBy=popularity&'
               'language=en&'
               'apiKey='+API_KEY)

        response = requests.get(url)
        r = response.json()
        if(r['totalResults'] >= 0):
            res = r['articles'][0:n]
            for ele in res:
                results.append(ele)

    results.sort(key=lambda x: x["publishedAt"])

    data = jsonify(results)
    return data


if __name__ == "__main__":
    app.run(debug=True)
