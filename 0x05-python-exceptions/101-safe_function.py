#!/usr/bin/python3
from decimal import DivisionByZero
from logging import exception


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
