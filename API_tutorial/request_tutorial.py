import requests
import json
import pprint

response = requests.get("https://randomuser.me/api/").json()
content = json.loads(response.content)
# pprint.pprint(content)
for data in content['results']:
    # pprint.pprint(data['location'])
    coordinates = [val if key == 'coordinates' else '' for key, val in data['location'].items()]
    # pprint.pprint(coordinates)
    for loc in coordinates:
        if loc:
            print(filter(lambda e: e[0]['latitude'], loc.items()))
