#!/usr/bin/python3
"reading a file in python"


def read_file(filename=""):
    "comment"
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
