import snowflake.connector
import os
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

conn = snowflake.connector.connect(
    user=os.environ['SF_USERNAME'],
    password=os.environ['SF_PASSWORD'],
    account=os.environ['SF_ACCOUNT']
    )
print(conn.user)
cursor = conn.cursor()
cursor.execute("SELECT * FROM DEV.RAW.TITANIC_TRAIN_RAW;")
print("connection is donne")
	