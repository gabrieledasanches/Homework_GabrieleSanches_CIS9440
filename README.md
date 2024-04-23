# Homework_GabrieleSanches_CIS9440

# Car Crashes in New York City 
### Motor Vehicle Collisions - Crashes

This project uses the data set for motor vehicles collisions from nyc open data (https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)


The data has 29 columns, and 2.07M rows and it includes details about crashes events, that were reported by the police. Each row describes one crash event, and have a collision ID to be uniquely identified. The columns provide information  about the collision such as date and time it occurred, the location (zip code, borough, street name), number os persons injured and killed, if the incident involved pedestrian or cyclists, the number that got injured or killed, contributing factors for the collision, and vehicle type.

## Table of Contents

- [Business Case](#business-case)
- [Business Requirements/Rules](#business-requirementsrules)
- [Information Architecture](#information-architecture)
- [Staging Area](#staging-area)
- [Data Modeling](#data-modeling)
- [ETL Process](#etl-process)
- [Data Mapping](#data-mapping)


**Business Case:**

A consulting firm specialized in analyzing and mitigating risks associated with motor vehicle collisions wants to analyze the Motor Vehicle Car Crashes data set to determine if the time the crash happened have a correlation with the number of people killed/injured and to find the top 5 contributing factor for crashes. 
    
The project aims to improve client satisfaction, create a stronger reputation for the company, and generate possible revenue growth from additional consulting engagements. 

**Business Requirements/Rules:**

- Acquire data from NYC Open Data
- Date should be in the following format: YYYY-MM-DD
- Time and date should be in separated colums
- Data set should include only 2021 data 
- Handle missing values
- Determine correlations between the time of the crash and the number of people killed or injured.
- Identify the top contributing factors for crashes.


**Information Architecture:** 

<img width="1341" alt="Screenshot 2024-04-22 at 11 47 16 PM" src="https://github.com/gabrieledasanches/Homework_GabrieleSanches_CIS9440/assets/159973139/5ebc37fd-e400-4798-a902-f480f267774f">



**Staging Area:** Microsoft Azure 

_Steps from extracting tha data to saving into Azure:_
    - To extract the data, I create a python script for web API using the requests library an dthe json package. I used the API from my data sourece (form open NYC data), extracted the data and created a csv file.
    - I chose to store the data in Azure as my storage of choice.  
    - To connect to Azure, I created a code that contained the key, container name, and blob name (file name).
    - After that configuration was done, I stored my csv file in the container. (The file stored was the raw data)


**Data Modeling:**

Used DB Schema to create the data model.
My satr schema contains 1 fact table called facts_crashes and 4 dimension tables: dim_date, dim_location, dim_vehicle_type, and dim_contributingfactors. All relationships are one to many. 

<img width="1029" alt="Screenshot 2024-04-22 at 11 42 11 PM" src="https://github.com/gabrieledasanches/Homework_GabrieleSanches_CIS9440/assets/159973139/c78f92b0-3ff2-4c92-9de4-88a435eaf19c">


**ETL Process:**

ETL Process: After having the data stored in Azure, I started the 


**Data Mapping:**
