#!/usr/bin/python3
"""
comment
"""


import sys
from urllib import parse, request

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    values = parse.urlencode(values).encode("utf-8")
    data = request.Request(url, values)
    with request.urlopen(data) as response:
        the_page = response.read().decode("utf-8")
        print(the_page)
