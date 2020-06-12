#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    line = ""
    for i in range(n):
        line += "#"
        print(line.rjust(n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
