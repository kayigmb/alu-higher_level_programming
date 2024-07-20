#!/usr/bin/python3
"comment"


def append_after(filename="", search_string="", new_string=""):
    "comment"
    with open(filename, "r") as f:
        data = f.readlines()

    with open(filename, "w") as fo:
        new_data = ""
        for line in data:
            new_data += line
            if search_string in line:
                new_data += new_string
        fo.write(new_data)
