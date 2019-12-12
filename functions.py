from urllib import parse
import pyodbc

def parse_url(url):
    """ Parce URL into dictionary for INPUT to Azure SQL server
    """
    # Parse URL String and capture query part
    url_query = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print (url_query)
    return url_query

def sqldb_conn(server, db, uid, pwd):
    """ Establish connection with the Azure SQL database
    """

    # Connect to the Azure SQL Database
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=azuresqlorange.database.windows.net;'
                        'Database=orange_azure;'
                        'Trusted_Connectoin=yes;'
                        'UID=orange;'
                        'PWD=Supermotdepasse!42;')
    cursor = conn.cursor()
    return conn, cursor