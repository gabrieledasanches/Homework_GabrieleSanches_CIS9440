# Car Crashes in New York City 

### Data
Found the data on NYC open data, and got the api url to use it in a python scripot to get the data

First, I checked if the code was working for 1000 rows only (script_tets.py), after I did the Web API for the full data set (webapi_data)

After getting the data, I got the data dictionary and stored it on github as well.

To do th edata modeling, I first got all of my columns names. After that I separated it into 'Facts' and 'Dimension' table. From the "general dimension tbale" I created many dimensions tables - location, date, time, vehicle, contributing factors. After that, i checked if all of my dimenension tables, and my facts tables were in first, second, and thrid normal form, and updated the keys as needed. 
