#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is None:
        tuple = (0, None)
    else:
        tuple = (len(sentence), sentence[0])
    return tuple
