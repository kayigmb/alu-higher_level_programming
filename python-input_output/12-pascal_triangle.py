#!/usr/bin/python3
"comment"


def pascal_triangle(n):
    "comment"
    if n <= 0:
        return []
    lists = [[1]]
    for i in range(1, n):
        l = lists[-1]
        t = [1]
        for i in range(len(l) - 1):
            t.append(l[i] + l[i + 1])
        lists.append(t)
        t.append(1)
    return lists
