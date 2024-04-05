# import Librairies
import pandas as pd
import numpy as  np
import json
import requests
import boto3
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from io import StringIO

# Functions
def azure_upload_blob(connect_str, container_name, blob_name, data):
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(data, overwrite=True)
    print(f"Uploaded to Azure Blob: {blob_name}")

def azure_download_blob(connect_str, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    download_stream = blob_client.download_blob()
    return download_stream.readall()


#Web API Code to get the data:
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

config_file_path = 'config/config.json'

#load the JSON configuration file
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

#definning the name of storgae, container, and blob
CONNECTION_STRING_AZURE_STORAGE = config["connectionString"]
CONTAINER_AZURE = 'carcrash'
blob_name = "car_crash.csv"

#Convert Dataframe to csv
output = StringIO()
df.to_csv(output, index=False)
data = output.getvalue()
output.close()

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING_AZURE_STORAGE)

# Get a blob client using the container name and blob name
blob_client = blob_service_client.get_blob_client(container=CONTAINER_AZURE, blob=blob_name)

# Upload the CSV data
blob_client.upload_blob(data, overwrite=True)

print(f"Uploaded {blob_name} to Azure Blob Storage in container {CONTAINER_AZURE}")
