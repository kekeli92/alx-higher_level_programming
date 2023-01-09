#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # ignore script name

    result = 0  # variable to hold adds
    for arg in args:
        result += int(arg)  # add command line arguments
    print("{}".format(result))
