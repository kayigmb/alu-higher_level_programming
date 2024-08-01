#!/usr/bin/python3
"""documeted"""

import sys

import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = "Gzoref"
    username = sys.argv[1]
    token = sys.argv[2]
    headers = {"Authorization": "token {}".format(token)}
    request = requests.get(url, headers=headers)
    print(request.json().get("id"))
