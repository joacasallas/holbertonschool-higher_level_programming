#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tuple = (0, None)
    else:
        tuple = (len(sentence), sentence[0])
    return tuple
