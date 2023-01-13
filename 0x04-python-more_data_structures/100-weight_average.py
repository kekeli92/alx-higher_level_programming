#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    first_sum = 0
    second_sum = 0

    for score, weight in my_list:
        first_sum += score * weight
        second_sum += weight
    return first_sum / second_sum
