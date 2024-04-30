# Homework_GabrieleSanches_CIS9440

# Car Crashes in New York City 
### Motor Vehicle Collisions - Crashes

This project uses the data set for motor vehicles collisions from nyc open data (https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)


The data has 29 columns, and 2.07M rows and it includes details about crashes events, that were reported by the police. Each row describes one crash event, and have a collision ID to be uniquely identified. The columns provide information  about the collision such as date and time it occurred, the location (zip code, borough, street name), number of persons injured and killed, if the incident involved pedestrians or cyclists, the number of people that got injured or killed, contributing factors for the collision, and vehicle type.

## Table of Contents

- [Business Case](#business-case)
- [Business Requirements/Rules](#business-requirementsrules)
- [Information Architecture](#information-architecture)
- [Staging Area](#staging-area)
- [Data Modeling](#data-modeling)
- [ETL Process](#etl-process)
- [Serving Data](#serving-data)


### Business Case

A consulting firm specializing in risk analysis and mitigation for motor vehicle collisions aims to leverage data-driven insights to enhance client services and expand its market presence. The firm has identified the Motor Vehicle Collisions dataset from NYC Open Data as a valuable resource for understanding the factors contributing to crashes and their impact on fatalities and injuries.

The project aims to leverage the Motor Vehicle Collisions dataset to conduct a comprehensive analysis of crash patterns, contributing factors, and their impact on fatalities, injuries, and property damage. Key objectives include:

- Crash Analysis:
      Explore the total number of accidents, fatalities, and injuries to understand overall trends and severity levels over time.
      Analyze temporal patterns in crash occurrence and severity using line charts to identify high-risk periods.
- Contributing Factor Identification:
      Identify and prioritize the top contributing factors for crashes using scatter plots to visualize relationships between factors and incident severity.
      Use interactive visuals to delve into contributing factors by vehicle type and accident frequency.
- Geospatial Analysis (Borough-Level):
      Utilize borough-level analysis to visualize crash distribution and highlight areas with higher incident rates.
- Temporal Trends:
      Analyze temporal trends in injuries and fatalities by year and month using heat maps to highlight seasonal variations and long-term patterns.
      Explore correlations between time of the crash and the number of people injured or killed using line charts.

### Business Requirements/Rules

- Acquire data from NYC Open Data
- Date should be in the following format: YYYY-MM-DD
- Time and date should be in separated colums
- Handle missing values
- Determine correlations between the time of the crash and the number of people killed or injured.
- Identify the top contributing factors for crashes
- Create a dashboard with analytical insights


### Information Architecture

<img width="1341" alt="Screenshot 2024-04-22 at 11 47 16 PM" src="https://github.com/gabrieledasanches/Homework_GabrieleSanches_CIS9440/assets/159973139/5ebc37fd-e400-4798-a902-f480f267774f">

1. Data Source: The data is sourced from the Motor Vehicle Collisions - Crashes dataset provided by NYC Open Data.
2. Storage: The raw data is stored in Microsoft Azure Storage
4. Database: Load the data into PostgreSQL database, which serves as the repository for the cleaned and transformed data.


### Staging Area

- Microsoft Azure 
- To connect to Azure, I created a code that contained the key, container name, and blob name (file name)
- After that configuration was done, I stored my csv file in the container. (The file stored was the raw data)


### Data Modeling

Used DB Schema to create the dimensional modeling .
My satr schema contains 1 fact table called facts_crashes and 4 dimension tables: dim_date, dim_location, dim_vehicle_type, and dim_contributingfactors. All relationships are one to many. 

<img width="1029" alt="Screenshot 2024-04-22 at 11 42 11 PM" src="https://github.com/gabrieledasanches/Homework_GabrieleSanches_CIS9440/assets/159973139/c78f92b0-3ff2-4c92-9de4-88a435eaf19c">


### ETL Process

- Extraction: Data is extracted from the Motor Vehicle Collisions - Crashes dataset provided by NYC Open Data using a Python script with web API functionality. The data is retrieved in JSON format and converted into a CSV file.
- Transformation: Upon extraction, the raw data undergoes cleaning and transformation. This involves handling missing values and duplicates, formatting dates and times, renaming columns, and creating "subsets" of the data. Transformation also includes data mapping: Each column from the source CSV file is mapped to the corresponding dataframes, based on the dimensional modeling, that will later be loaded into the corresponding PostgreSQL tables (dim_date, dim_location, dim_contributingfactors, dim_vehicle_type, facts_crashes).
- Loading: The cleaned and transformed data is loaded into the PostgreSQL database using SQL commands. Separate tables are created for each dimension (dim_date, dim_location, dim_vehicle_type, dim_contributingfactors) and the fact table (facts_crashes).


### Serving Data

Interactive Tableau Dahsboard (filter all visuals by year of the crash) https://public.tableau.com/app/profile/gabriele.sanches/viz/car_crashes_NYC/Dashboard1#1 
- Number of accidents 
- Number of fatalities
- Number of injuries
- Vehicle type vs. number of accidents (top 10)
- Contributing factors for crashes
- Crashes by borough
- Total number of victims injured by year and month
- Number of people injured vs. time of the crash
- Total number of victims killed by year and month 
- Number of people killed vs. time of the crash
