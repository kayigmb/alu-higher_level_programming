#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list.copy()
    for idx, item in enumerate(n_list):
        if item == search:
            n_list[idx] = replace
    return n_list
