import requests
import json

def getArticles(query,n):
    API_KEY = 'dc7fb1d2a4c44ceabd4173d71cacb27a'
    
    url = ('https://newsapi.org/v2/everything?'
        'q='+ query+'&'
        'from=2022-03-03&' ##need to change based on current date
        'sortBy=popularity&'
        'language=en&'
        'apiKey='+API_KEY)


    response = requests.get(url)
    r = response.json()
    ##print(r)
    if(r['totalResults'] > 0):
        ##print(r)
        return(r['articles'][0:n])
        ##print(r['articles'][1]['title'])
    else:
        print("no news found!")
        return(-1)


def getFeed(interests, n):
    results = []
    for query in interests: 
        r = getArticles(query,n)
        ##print(r)
        if( r == -1):
            continue
        for ele in r:
            results.append(ele)

    results = results
    results.sort(key=lambda x: x["publishedAt"])

    print(len(results))
    print(results)

    ##uncomment me to save the results file
    """
    json_object = json.dumps(results, indent = 4)
    with open(query+".json", "w") as outfile:
        outfile.write(json_object)
    """
    return results

def main():
    n = 2
    interests = ['Kpop', 'Artificial Intelligence', 'India']
    results = getFeed(interests, n)

if __name__ == '__main__':
    main()