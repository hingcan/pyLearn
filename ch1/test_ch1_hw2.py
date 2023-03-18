import requests

# Define the API endpoint and query parameters
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {'q': 'New York', 'appid': '5b935dc8f18aaf8b13419b6179bb596d'}

# Make the HTTP GET request and store the response in a variable
response = requests.get(url, params=params)

# Check if the request was successful (HTTP status code 200)
#if response.status_code == 200:
    # Print the response content
    #print(response.json())
#else:
    # Print an error message
    #print('Error:', response.status_code)


def test_check_response_status():
    response_status = response.status_code

    assert response_status == 200