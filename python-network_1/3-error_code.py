#!/usr/bin/python3
"""
comment
"""


import sys
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
