from urllib import parse

def parse_url(url):
    """ Parce URL into dictionary for INPUT to Azure SQL server
    """
    # Parse URL String and capture query part
    url_query = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print (url_query)
    return url_query