import psycopg2
import pandas as pd
import json

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def test_connection(config):
    """ function to test connection """
    try:
        connection = psycopg2.connect(**config)
        print("connection established")
        return connection
    except psycopg2.Error as e:
        print(f"Error establishing connection: {e}")
        return None



def test_sql_code(cursor):
    """ function that will test to create a table in azure env (sql) """
    
    create_schema = """CREATE SCHEMA IF NOT EXISTS "carcrash";"""
    
    create_table_contribfactors = """
        CREATE  TABLE "carcrash".dim_contributingfactors ( 
            contributingfactor_id BIGINT  NOT NULL  ,
            contributing_factor  VARCHAR(255)    ,
            CONSTRAINT pk_dim_contributingfactors PRIMARY KEY ( contributingfactor_id )
    );"""


    create_table_date = """
        CREATE TABLE "carcrash".dim_date ( 
            date_id              BIGINT  NOT NULL  ,
            date_iso_format      DATE    ,
            year_number          INT    ,
            quarter_number       INT    ,
            month_number         INT    ,
            month_name           VARCHAR(50)    ,
            day_number           INT    ,
            day_name             VARCHAR(50)    ,
            hour_number          INT    ,
            week_of_month        INT    ,
            week_of_year         INT    ,
            CONSTRAINT pk_dim_date PRIMARY KEY ( date_id )
    );"""

    create_table_location = """
        CREATE  TABLE "carcrash".dim_location ( 
            location_id          BIGINT  NOT NULL  ,
            borough              VARCHAR(255)    ,
            latitude             DECIMAL(10,2)   ,
            longitude            DECIMAL(10,2)   ,
            zip_code             INT    ,
            on_street_name       VARCHAR(255)    ,
            off_street_name      VARCHAR(255)    ,
            CONSTRAINT pk_dim_location PRIMARY KEY ( location_id )
    );"""

    create_table_vehcile_type = """
        CREATE  TABLE "carcrash".dim_vehicle_type ( 
            vehicle_id           BIGINT  NOT NULL  ,
            vehicle_type_code    VARCHAR(255)    ,
            CONSTRAINT pk_dim_vehicle_type PRIMARY KEY ( vehicle_id )
        );""" 


    create_table_facts = """
        CREATE  TABLE "carcrash".facts_crashes ( 
            fact_id BIGINT  NOT NULL  ,
            number_of_persons_injured INT,
            number_of_persons_killed INT,
            number_of_pedestrians_injured INT    ,
            number_of_pedestrians_killed INT    ,
            number_of_cyclist_injured INT    ,
            number_of_cyclist_killed INT    ,
            number_of_motorist_injured INT    ,
            number_of_motorist_killed INT    ,
            location_id INT,
            date_id BIGINT,
            vahicle_id INT,
            contributing_factor_id INT,
            CONSTRAINT pk_facts_crashes PRIMARY KEY(fact_id)
        );"""
    
    test_pull = """
        SELECT * FROM carcrash.dim_contributingfactors"""

    
    try:
        cursor.execute(create_table_contribfactors)
        print("craeted contri table!")
    except psycopg2.Error as e:
        print(f"error with code: {e}")


def fetch_data_from_db(cursor):
    """ function that will retrieve or fetch data from the database in pgadmin"""

    sql_query = """
    insert query in these quotes
    """

    try:
        cursor.execute(sql_query)
        data = cursor.fetchall()
        # this code is to get the first row from your data which is technically the headers or column names
        # columns = [desc[0] for desc in cursor.description]
        # return columns

        # if you want to store the data as a dataframe - you will have to add the headers to the dataframe with an argumetn
        # df = pd.DataFrame(data) # add: name=columns, to add columsn to your data frame
       # print(df)

    
    except psycopg2.Error as e:
        print(f"Error retrieving data from the db: {e}")
    

# Load config from file
config = load_config('config_dw.json')

# Establish connection using loaded config
connection = test_connection(config)

if connection:
    with connection:
        with connection.cursor() as cursor:
            # insert function that has the SQL code to test
            test_sql_code(cursor)


