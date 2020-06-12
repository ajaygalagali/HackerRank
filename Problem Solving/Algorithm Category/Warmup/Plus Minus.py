#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr, n):
    neg = 0
    pos = 0
    ze = 0
    for i in range(n):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
        else:
            ze += 1

    print(pos / n)
    print(neg / n)
    print(ze / n)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
