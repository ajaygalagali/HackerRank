#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    brr = arr

    plus = []

    for i in range(0, len(brr)):
        a = arr.pop()

        plus.append(sum(arr))
        arr.insert(0, a)

    print(min(plus), max(plus))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
