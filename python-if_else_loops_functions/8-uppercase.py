#!/usr/bin/python3
def uppercase(str):
    n_str = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            n_str += chr(ord(c) - 32)
        else:
            n_str += c
    print("{}".format(n_str))
