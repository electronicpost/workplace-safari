import requests

url='https://wps-tvmaze.azurewebsites.net/api/submit'

query_string = {
    "name": "Mick",
    "show_id":  "17078"
}

response = requests.get(url, params=query_string)

print(response, response.text)