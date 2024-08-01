#!/usr/bin/python3
"comment"
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
