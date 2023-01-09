#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(10):
        if first_num < second_num:
            print("{:01d}{:01d}".format(first_num, second_num), end=", "
                  if first_num < 8 or second_num < 9 else "\n")
