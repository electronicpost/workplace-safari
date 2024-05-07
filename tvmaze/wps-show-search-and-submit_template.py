import requests

URL_SEARCH = 'https://api.tvmaze.com/search/shows'
URL_SUBMIT = 'https://wps-tvmaze.azurewebsites.net/api/submit'

# Complete PART ONE instructions in SECTIONS A, B, and C (estimated 8 lines of code)
# Complete PART TWO instructions in SECTIONS B, and C (estimated 14 lines of code in total)
# Complete PART THREE instructions in SECTIONS A, and D (estimated 22 lines of code in total)


# SECTION A
# PART ONE: Define (string) variables for name and show_id
# ----------------------------------------------
# PART THREE: Define variables for name and show_search, comment out show_id

# ==============================================
# SECTION A CODE


# ==============================================

# SECTION B
# PART ONE:
# Define a PROCEDURE api_request() that takes a URL and query string dictionary as parameters
# The PROCEDURE makes a request using requests.get()
# The PROCEDURE then prints the response, query string and response text
# ----------------------------------------------
# PART TWO:
# Adjust the PROCEDURE into a FUNCTION api_request() that takes the following as parameters
# A URL, query string dictionary and a response content type to be returned (text/json)
# Set a default value for the response content type making this an optional parameter
# Use an IF statement to return the response content as either text or JSON

# ==============================================
# SECTION B CODE


# ==============================================

# SECTION D
# PART THREE:
# Make a TV Show SEARCH request via a call to the api_request() FUNCTION (with a JSON response)
# Verify the search was successful (Try-Except) and extract the show_id from the search results

# ==============================================
# SECTION D CODE


# ==============================================

# SECTION C
# PART ONE:
# Build query string dictionary for parameters 'name' and 'show_id'
# Make a TV Show SUBMIT request via a call to the api_request() PROCEDURE
# Parameters to submit: URL_SUBMIT, query_string
# ----------------------------------------------
# PART TWO:
# Contain the current code within an IF (conditional) statement to check if show_id is not equal to None
# Call the FUNCTION and store the returned content in a variable
# Print the variable

# ==============================================
# SECTION C CODE


# ==============================================