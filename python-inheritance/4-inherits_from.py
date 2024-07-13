#!/usr/bin/python3
"comment"


def inherits_from(obj, a_class):
    """comment"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
