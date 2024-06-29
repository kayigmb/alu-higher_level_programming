#!/usr/bin/python3
def multiple_returns(sentence):
    og_tuple = ()
    if len(sentence) == 0:
        og_tuple = 0, "None"
    else:
        og_tuple = len(sentence), sentence[0]
    return og_tuple
