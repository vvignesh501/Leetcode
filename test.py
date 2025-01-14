import json

import requests


def retrieve_results():
    response = requests.post('https://ancient-wood-1161.getsandbox.com:443/results', json=True)
    results = response.content

    converted_json = list(json.loads(results).values())[0]
    #print(converted_json)
    #ordered_json = sorted(converted_json, key=converted_json['publicationDate'])
    #print(ordered_json)

    #dict(sorted(.items(), key=lambda item: item[1]))


    #print(converted_json.sort(key=lambda item: item['publicationDate'], reverse=True))


def retrieve_results():
    response = requests.post('https://ancient-wood-1161.getsandbox.com:443/results', json=True)
    results = response.content
    converted_json = list(json.loads(results).values())
    print(converted_json)


retrieve_results()








retrieve_results()