# import libraries
from urllib import parse

# Set URL
url = 'https://www.yws.com?user_id=11&movie_id=111&comment=asdf'

# Parse URL String and capture query part
query_dict = dict(parse.parse_qsl(parse.urlsplit(url).query))
print (query_dict)