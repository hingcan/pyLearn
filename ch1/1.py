import requests
import time

# Set the API endpoint and your API key
endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "5b935dc8f18aaf8b13419b6179bb596d"

# Set the city ID for the location you want to get weather data for
city_id = 5128581

while True:
    # Make the API request
    response = requests.get(endpoint, params={"id": city_id, "units": "imperial", "appid": api_key})

    # Check the status code of the response
    if response.status_code == 200:
        # If the request is successful, print the data to the console
        data = response.json()
        print(data)
    else:
        # If the request is unsuccessful, print an error message
        print("Error: {}".format(response.status_code))

    # Wait 10 minutes before making the next request
    time.sleep(600)
