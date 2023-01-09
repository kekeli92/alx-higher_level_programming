#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)
    return multiple
