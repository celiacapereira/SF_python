import snowflake.connector
import os
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

conn = snowflake.connector.connect(
    user=os.environ['user'],
    password=os.environ['password'],
    account=os.environ['account']
    )

