import pandas as pd
import numpy as np
import json
import requests
from io import StringIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from math import ceil
import datetime
import calendar
from sqlalchemy import create_engine


# Specify the path to your JSON configuration file
config_file_path = "/Users/gabisanches/Desktop/CIS9440 - Data Warehouse/Homework/Homework_GabrieleSanches_CIS9440/scripts/config.json"

# Load the JSON configuration file
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)


CONNECTION_STRING_AZURE_STORAGE = config["connectionString"]
CONTAINER_AZURE = 'carcrash'

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING_AZURE_STORAGE)
# Get the container client
container_client = blob_service_client.get_container_client(CONTAINER_AZURE)


car_crash_df = pd.DataFrame()

# List all blobs in the specified container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print(blob.name)
    blob_client = container_client.get_blob_client(blob=blob.name)
    blob_data = blob_client.download_blob()
    blob_content = blob_data.readall().decode('utf-8')
    df = pd.read_csv(StringIO(blob_content))
    # Display the head of the DataFrame
    print(df.shape)
    # sind I have only one csv, I am doing to do the following instructions
    car_crash_df = df.copy()

#see columns names
car_crash_df.column()

#see fist few rows
car_crash_df.head()