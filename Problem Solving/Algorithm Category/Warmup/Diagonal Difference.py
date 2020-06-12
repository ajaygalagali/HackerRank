#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    # Write your code here

    d_one = 0
    d_two = 0
    w = n - 1
    for i in range(n):
        for j in range(n):
            if i == j:
                d_one = d_one + arr[i][j]

            if j == w:
                d_two = d_two + arr[i][j]

        w -= 1
    op = abs(d_one - d_two)
    return op


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
