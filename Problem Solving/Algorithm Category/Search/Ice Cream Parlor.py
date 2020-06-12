#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the icecreamParlor function below.
def icecreamParlor(m, cost):
    costInput = []
    costInput.extend(cost)

    l = len(cost)
    flag = 0
    for i in range(l):
        for j in range(1, l):

            if cost[0] + cost[j] == m:
                flag = 1
                if (costInput.index(cost[0]) == costInput.index(cost[j])):
                    tobe = costInput.index(cost[j])
                    costInput.insert(tobe, -1)
                    print(tobe + 1, costInput.index(cost[0]) + 1)
                else:
                    print(costInput.index(cost[0]) + 1, costInput.index(cost[j]) + 1)
            if flag == 1:
                break
        if flag == 1:
            break

        poped = cost.pop(0)
        cost.append(poped)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        icecreamParlor(m, arr)


