# import libraries
import pandas as pd
from functions import parse_url, sqldb_conn
import config

# Set URL
url = 'https://www.yws.com?user_id=11&movie_id=111&comment=asdf'

url_query = parse_url(url)

server = config.cf['server']
db = config.cf['db']
uid = config.cf['uid']
pwd= config.cf['pwd']

conn, cursor = sqldb_conn(server, db, uid, pwd)

query = """SELECT TOP 10 year, COUNT(year) AS count
            FROM analysis_movies
            GROUP BY year
            ORDER BY count DESC
            """

MostBestMovieYear = pd.read_sql(query, conn)
print(MostBestMovieYear)


# # Create a new record
# sql_insert = """
#             INSERT INTO cc_comments (user_id, movie_id, comment)
#             VALUES (?, ?, ?)
#             """

# # Execute the query and write to Azure DB table
# cursor.execute(sql_insert, url_query['user_id'], url_query['movie_id'], url_query['comment'])

# # Commit the connection since it is not autocimmited by default
# conn.commit()

# # Close the connection
# conn.close()