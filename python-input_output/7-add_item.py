#!/usr/bin/python3
"comment"
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    list_data = load_from_json_file("add_item.json")
except Exception:
    list_data = []

for arg in sys.argv[1:]:
    list_data.append(arg)
save_to_json_file(list_data, "add_item.json")
