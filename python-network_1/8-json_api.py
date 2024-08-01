#!/usr/bin/python3
"""documeted"""

import sys

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    arg_length = len(sys.argv)
    if arg_length == 2:
        q = sys.argv[1]
    else:
        q = ""
    request = requests.post(url, data={"q": q})
    try:
        request = request.json()
        if not request:
            print("No result")
        else:
            print("[{}] {}".format(request["id"], request["name"]))
    except ValueError:
        print("Not a valid JSON")
