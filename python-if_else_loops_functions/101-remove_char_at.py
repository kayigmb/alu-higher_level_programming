#!/usr/bin/python3
def remove_char_at(str, n):
    another = ""
    if len(str) == 0:
        return str
    for i in range(len(str)):
        if i != n:
            another += str[i]
    return another


if __name__ == "__main__":
    print(remove_char_at("Holberton School", 3))
