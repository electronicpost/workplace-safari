import requests, json

host = 'https://api.tvmaze.com'
resource = '/search/shows'

params = {'q': 'pepper pig'}

response = requests.get(host + resource, params=params)
print(response)

json_response = json.loads(response.text)
print(len(json_response))
for show in json_response:
    print(show['show']['name'], show['show']['id'])
    #if show['show']['name'] == 'The Simpsons':
    #    print(json.dumps(show, indent=2))
#print(json.dumps(json_response, indent=2))
