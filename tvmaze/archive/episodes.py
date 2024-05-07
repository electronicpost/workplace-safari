import requests, json

host = 'https://api.tvmaze.com'
resource = '/shows/4972/episodes'

response = requests.get(host + resource)
print(response)

json_response = json.loads(response.text)
print(len(json_response))
#print(json.dumps(json_response, indent=2))
episode_count = 0
for item in json_response:
    episode_count = episode_count + 1
    print(f"[ {episode_count} ] {item['name']}, (Season: {item['season']}, Episode Number: {item['number']})")
#    if show['show']['name'] == 'The Simpsons':
#        print(json.dumps(show, indent=2))

