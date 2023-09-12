#!/usr/bin/python3
def is_divisible(x):
    return x % 2 == 0


def divisible_by_2(my_list=[]):
    result = list(map(is_divisible, my_list))
    return result
