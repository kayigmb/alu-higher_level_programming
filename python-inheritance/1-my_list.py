#!/usr/bin/python3
""""List """


class MyList(list):
    """class"""

    def print_sorted(self):
        """print"""
        temp = self[:]
        temp.sort()
        print("{}".format(temp))
