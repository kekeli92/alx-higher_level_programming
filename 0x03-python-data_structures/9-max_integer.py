#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    elif my_list:
        curr_max_num = my_list[0]

        for number in my_list:
            if number > curr_max_num:
                curr_max_num = number
        return curr_max_num
