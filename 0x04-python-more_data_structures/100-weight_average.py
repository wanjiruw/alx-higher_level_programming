#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    scores = sum(map(lambda x: x[0] * x[1], my_list))
    total_weight = sum([x[1] for x in my_list])
    return scores / total_weight
