#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    arr = bill
    arr.pop(k)
    s = sum(arr)
    spl = s//2
    owe = b - spl
    if spl == b:
        print("Bon Appetit")
    else:
        print(str(owe))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
