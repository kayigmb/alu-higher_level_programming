#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    sum = 0
    for elem in my_list:
        if elem in unique:
            continue
        else:
            unique.append(elem)
    for item in unique:
        sum += item
    return sum
