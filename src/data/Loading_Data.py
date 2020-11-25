import os
import pandas as pd
import sqlite3

def load_data(query):
    '''
    Retrieve data for year/location/group from the internet
    and return data (or write data to file, if `outpath` is
    not `None`).
    '''
    path = os.path.join( "battery_use-000025.db")
    conn = sqlite3.connect(path)
    table = pd.read_sql_query(query, conn)
    table.to_csv('./src/data/battery_use_data.csv')
    return table

