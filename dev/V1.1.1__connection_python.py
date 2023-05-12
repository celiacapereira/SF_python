import os
import snowflake.connector
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
# import SF_python.test.connection as d
from testes.connection import df_drop


print(df_drop)
account = os.environ['SF_ACCOUNT']
password = os.environ['SF_PASSWORD']
username= os.environ['SF_USERNAME']


# print(f"SF ACCOUNT IS:  {account}")
# print(f"SF PASSWORD IS:  {password}")
# print(f"SF USERNAME IS:  {username}")

print("Estamos na pasta dev")

conn = snowflake.connector.connect (
    user=username,
    password=password,
    account=account

)
cursor = conn.cursor()

conn.cursor().execute("USE WAREHOUSE COMPUTE_WH;")

conn.cursor().execute("CREATE OR REPLACE SCHEMA DEV.REPORT; ")

conn.cursor().execute(""" CREATE TABLE DEV.REPORT.TITANIC_REPORT (
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
            conn=conn,
            df=d,
            table_name='TITANIC_REPORT',
            database='DEV',
            schema='REPORT'
        )
cursor.close()

