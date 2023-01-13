#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    constant = 2
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] *= constant
    return new_dict
