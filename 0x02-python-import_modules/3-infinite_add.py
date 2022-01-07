#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    import sys
    number = 0
    for i in range(1, len(sys.argv)):
        number = add(number, int(sys.argv[i]))
    print(number)
