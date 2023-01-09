#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    # Check if there are three command line arguments
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Dictionary mapping operator values to functions
    op_func = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }

    # Get operands and operator
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    # Check if operator is valid
    if op not in op_func:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform operation and print result
    result = op_func[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))
