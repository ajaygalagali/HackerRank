#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(height, string):
    maxHeight = 0
    lenString = len(string)
    for i in string:
        position = ord(i)-97


        if height[position] > maxHeight:
            maxHeight = height[position]
        print(maxHeight)
    result = maxHeight*lenString
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
