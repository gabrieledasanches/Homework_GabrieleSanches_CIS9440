
import psycopg2

"""

export PGHOST=cis9440spring2024.postgres.database.azure.com
export PGUSER=GABRIELEDAMELIOSANCHES
export PGPORT=5432
export PGDATABASE=postgres
export PGPASSWORD=Nyc3604! 


"""

def test_connection():
    """ function to test SQL code """

    try:
        connection = psycopg2.connect(
            database='postgres',
            user='GABRIELEDAMELIOSANCHES',
            password='Nyc3604!',
            host='cis9440spring2024.postgres.database.azure.com',
            port='5432'
        )
    
        print("connection established")
        return connection
    except psycopg2.Error as e:
        print(f"Error establshing connection: {e}")
        return None


def test_sql_code(cursor):
    """ function that will test to create a table in azure env (sql) """
    
    create_tx = """
    CREATE  TABLE test ( 
        CONTRIBUTINGFACTOR_ID integer NOT NULL   ,
        CONTRIBUTING_FACTOR  varchar(255)    ,
        CONSTRAINT PK_DIM_CONTRIBUTINGFACTORS PRIMARY KEY ( CONTRIBUTINGFACTOR_ID )
    );"""

    try:
        cursor.execute(create_tx)
        connection.commit()
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")



connection = test_connection()
with connection:
    with connection.cursor() as cursor:
        # insert function that has the SQL code to test
        test_sql_code(cursor)



