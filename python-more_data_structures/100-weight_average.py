#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    d = 0
    if my_list == []:
        return 0
    for elem in my_list:
        total += elem[0] * elem[1]
        d += elem[1]
    return total / d
