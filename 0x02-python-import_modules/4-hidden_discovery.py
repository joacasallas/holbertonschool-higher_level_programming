#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    for i in range(1, len(sys.argv)):
        if sys.argv[i] != "_":
            print(sys.argv[i])
