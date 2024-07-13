#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for n in range(x):
        try:
            numb = my_list[n]
            print("{:d}".format(numb), end="")
            num = num + 1
        except (ValueError, TypeError):
            continue
    print()
    return num
