#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # get the first elements of the tuples
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0

    # get the second elements of the tuples
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # return the tuple with the sum of the elements
    return (a1 + b1, a2 + b2)
