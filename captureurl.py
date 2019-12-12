# import libraries
from urllib import parse
import pyodbc
import pandas as pd

# Set URL
url = 'https://www.yws.com?user_id=11&movie_id=111&comment=asdf'

# Parse URL String and capture query part
url_query = dict(parse.parse_qsl(parse.urlsplit(url).query))
print (url_query)

# Connect to the Azure SQL Database
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=azuresqlorange.database.windows.net;'
                      'Database=orange_azure;'
                      'Trusted_Connectoin=yes;'
                      'UID=orange;'
                      'PWD=Supermotdepasse!42;')

cursor = conn.cursor()

# Create a new record
sql_insert = """
            INSERT INTO cc_comments (user_id, movie_id, comment)
            VALUES (?, ?, ?)
            """

# Execute the query and write to Azure DB table
cursor.execute(sql_insert, url_query['user_id'], url_query['movie_id'], url_query['comment'])

# Commit the connection since it is not autocimmited by default
conn.commit()

# Close the connection
conn.close()