# import libraries
from functions import parse_url, sqldb_conn, query
import config

# Set URL
url = 'https://www.yws.com?user_id=11&movie_id=111&comment=asdf'
url_query = parse_url(url)

# Connect to the Azure SQL database
driver = config.DRIVER
server = config.SERVER
db = config.DB
uid = config.UID
pwd= config.PWD
conn, cursor = sqldb_conn(driver, server, db, uid, pwd)

# Create a new record
sql_insert = query()

# Execute the query and write to Azure DB table
cursor.execute(sql_insert, url_query['user_id'], url_query['movie_id'], url_query['comment'])

# Commit the connection since it is not autocimmited by default
conn.commit()

# Close the connection
conn.close()