import requests

URL_SEARCH = 'https://api.tvmaze.com/search/shows'
URL_SUBMIT = 'https://wps-tvmaze.azurewebsites.net/api/submit'

# Search parameters
name = 'Mick'
show_search = 'fallout'

# Function to make API requests
def api_request(url, query_string, return_me='text'):
    response = requests.get(url, params=query_string)
    print(f'{response} {query_string}')
    if return_me == 'json':
        response_content = response.json()
    elif return_me == 'text':
        response_content = response.text
    return response_content

# Search for TV show
search_query_str = {
        'q': show_search
    }
tv_show_search = api_request(URL_SEARCH, search_query_str, 'json')
try:
    show_id = tv_show_search[0]['show']['id']
    print('Top search result:', tv_show_search[0]['show']['name'])
except(IndexError):
    show_id = None
    print('No show found, please try again with a different search term than', show_search)

# Submit TV show for report processing
if show_id != None:
    query_string = {
        'name': name,
        'show_id': str(show_id)
    }
    tv_show_submit = api_request(URL_SUBMIT, query_string)
    print(tv_show_submit)
