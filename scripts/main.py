import json

config_file_path = 'config/config.json'

#load the JSON configuration file
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

Connection_STRING = config["connectionString"]