import requests

url='https://wps-tvmaze.azurewebsites.net/api/submit'

# Build query string for parameters 'name' and 'show_id'

id = 100

#for id in range(100, 20000):
query_string = {
        'name': 'Mick',
        'show_id': str(id)
    }

    # Make request using requests.get() 

response = requests.get(url, params=query_string)
    
print(response, response.text)

    # Print response code and response text



# Print response code and response text



