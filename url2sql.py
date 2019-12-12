# import libraries
import pandas as pd
from functions import parse_url, sqldb_conn, query
import config

# Set URL
url = 'https://www.yws.com?user_id=11&movie_id=111&comment=asdf'
url_query = parse_url(url)

# Connect to the Azure SQL database
server = config.cf['server']
db = config.cf['db']
uid = config.cf['uid']
pwd= config.cf['pwd']
conn, cursor = sqldb_conn(server, db, uid, pwd)

# Create a new record
sql_insert = query()

# Execute the query and write to Azure DB table
cursor.execute(sql_insert, url_query['user_id'], url_query['movie_id'], url_query['comment'])

# Commit the connection since it is not autocimmited by default
conn.commit()

# Close the connection
conn.close()