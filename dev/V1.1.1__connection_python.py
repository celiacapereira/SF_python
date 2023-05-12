import os
import snowflake.connector
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import testes.connection as d

account = os.environ['SF_ACCOUNT']
password = os.environ['SF_PASSWORD']
username= os.environ['SF_USERNAME']


print(f"SF ACCOUNT IS:  {account}")
print(f"SF PASSWORD IS:  {password}")
print(f"SF USERNAME IS:  {username}")

print("Estamos na pasta dev")

connection = snowflake.connector.connect (
    user=username,
    password=password,
    account=account

)
cursor = connection.cursor()

connection.cursor().execute("USE WAREHOUSE COMPUTE_WH;")

connection.cursor().execute("CREATE OR REPLACE SCHEMA DEV.REPORT; ")

connection.cursor().execute(""" CREATE TABLE DEV.REPORT.TITANIC_REPORT (
    PASSENGERID INT,
    SURVIVED INT, 
    PCLASS INT, 
    SEX VARCHAR(6), 
    AGE INT, 
    SIBSP INT, 
    PARCH INT, 
    AGERANGE VARCHAR(5)
    )""")


success, num_chunks, num_rows, output = write_pandas(
            conn=connection,
            df=d.df_drop,
            table_name='TITANIC_REPORT',
            database='DEV',
            schema='REPORT'
        )
cursor.close()