#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    res_add = add(a, b)
    print("{} + {} = {}".format(a, b, res_add))

    res_sub = sub(a, b)
    print("{} - {} = {}".format(a, b, res_sub))

    res_mul = mul(a, b)
    print("{} * {} = {}".format(a, b, res_mul))

    res_div = div(a, b)
    print("{} / {} = {:.0f}".format(a, b, res_div))
