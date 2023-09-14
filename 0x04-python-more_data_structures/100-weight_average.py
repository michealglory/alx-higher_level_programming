#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        denominator = 0
        for tuple in my_list:
            number += (tuple[0] * tuple[1])
            denominator += (tuple[1])
        return (number/denominator)
    return 0
