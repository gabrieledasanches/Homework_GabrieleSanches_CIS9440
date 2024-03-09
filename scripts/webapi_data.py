import requests
import json
import pandas as pd

def check_url(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response
    else:
        print("Bad connection")
        return None

url = 'https://data.cityofnewyork.us/resource/h9gi-nx95.json'

# Set the limit per request
limit_per_request = 2000

# Initialize variables
offset = 0
all_data = []

while True:
    params = {'$limit': limit_per_request, '$offset': offset}
    data = check_url(url, params)

    if data:
        current_data = data.json()
        if not current_data:
            break

        all_data.extend(current_data)
        offset += limit_per_request
    else:
        print("not working")
        break

# Convert the JSON data to a Pandas DataFrame
df = pd.DataFrame(all_data)

# Save to a CSV file
df.to_csv("car_crash.csv", index=False)
print("file created successfully.")
