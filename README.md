# Homework_GabrieleSanches_CIS9440

# Car Crashes in New York City 
### Motor Vehicle Collisions - Crashes

This project uses the data set for motor vehicles collisions from nyc open data https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data

The data has 29 columns, and 2.07M rows and it includes details about crashes events, that were reported by the police. Each row describes one crash event, and have a collision ID to be uniquely identified. The columns provide information  about the collision such as date and time it occurred, the location (zip code, borough, street name), number os persons injured and killed, if the incident involved pedestrian or cyclists, the number that got injured or killed, contributing factors for the collision, and vehicle type.


Business Case: 
    A consulting firm specialized in analyzing and mitigating risks associated with motor vehicle collisions wants to analyze the Motor Vehicle Car Crashes data set to determine if the time the crash happened have a correlation with the number of people killed/injured and to find the top 5 contributing factor for crashes. 
    The project aims to improve client satisfaction, create a stronger reputation for the company, and generate possible revenue growth from additional consulting engagements. 

Business Requirements/Rules:
    - Acquire data from NYC Open Data
    - Date should be in the following format: YYYY-MM-DD
    - Time and date should be in separated colums
    - Data set should include only 2021 data 
    - Handle missing values
    - Determine correlations between the time of the crash and the number of people killed or injured.
    - Identify the top contributing factors for crashes.


Information Architectue: inside "docs" folder

Staging Area: Microsoft Azure 

Steps from extracting tha data to saving into Azure:
    - To extract the data, I create a python script for web API using the requests library an dthe json package. I used the API from my data sourece (form open NYC data), extracted the data and created a csv file.

    - I chose to store the data in Azure as my storage of choice. I chose this storage for the convenience of price and easy accessibility. 

    - To connect to Azure, I created a code that contained the key (stored privatly in the config folder), teh container name, and blob name (file name).

    - After that configuration was done, I stored my csv file in the container. (The file stored was the raw data)

    - Data Cleaning: Cleaned the data and stored the clean data on the Axure Container. 

Data Mapping
ETL OR ELT Process: