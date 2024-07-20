#!/usr/bin/python3
"comment"
import json


def load_from_json_file(filename):
    "comment"
    with open(filename, "r", encoding="UTF8") as data:
        return json.load(data)
