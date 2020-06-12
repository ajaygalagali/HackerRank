#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_points = 0
    b_points = 0

    if a[0] > b[0]:
        a_points += 1
    elif a[0] < b[0]:
        b_points += 1
    else:
        pass

    if a[1] > b[1]:
        a_points += 1
    elif a[1] < b[1]:
        b_points += 1
    else:
        pass

    if a[2] > b[2]:
        a_points += 1
    elif a[2] < b[2]:
        b_points += 1
    else:
        pass

    points = [a_points, b_points]
    return points


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
