#!/usr/bin/python3
"""documeted"""


import sys

import requests

if __name__ == "__main__":
    data = requests.get(sys.argv[1])
    stat_code = data.status_code
    if stat_code > 400:
        print("Error code: {}".format(stat_code))
    else:
        print("{}".format(data.text))
