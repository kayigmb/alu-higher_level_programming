#!/usr/bin/python3
"""comment"""
import urllib.request

if __name__ == "__main__":
    y = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(y) as re:
        data = re.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode("utf-8")}")
