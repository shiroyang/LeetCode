#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    cost_idx = {val:idx for idx, val in enumerate(cost, 1)}
    for idx, price in enumerate(cost, 1):
        rem = money - price
        if cost_idx.get(rem):
            if idx == cost_idx.get(rem): continue
            print(idx, cost_idx.get(rem))
            break  

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
