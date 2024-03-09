import requests 
import json
import pandas as pd


def check_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
           
    else:
        print("bad connection")
        return None


url = 'https://data.cityofnewyork.us/resource/h9gi-nx95.json'
data = check_url(url)

if data:
    print("cleared")
    current_data = data.json()
    df = pd.DataFrame(current_data).to_csv("car_crash_test.csv", index=False)