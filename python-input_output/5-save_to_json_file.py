#!/usr/bin/python3
"comment"
import json


def save_to_json_file(my_obj, filename):
    """comment"""
    with open(filename, "w", encoding="UTF8") as data:
        data.write(json.dumps(my_obj))
