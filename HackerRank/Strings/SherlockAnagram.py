#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    # abc -> {a:1, b:1, c:1} -> {1:3}
    # abcc -> {a:1, b:1, c:2} -> {1:2, 2:1}
    # aabbcd -> {a:2, b:2, c:1, d:1} -> {1:2, 2:2}
    # aabbc -> {a:2, b:2, c:1} -> {1:1, 2:2}
    from collections import Counter
    char_cnt = Counter(s)
    freq = Counter(char_cnt.values())
    if len(freq) == 1: return "YES"
    if len(freq) > 2: return "NO"
    A = sorted(list(freq.items()))
    if (A[0][0] + 1 == A[1][0] and A[1][1] == 1) or (A[0] == (1, 1)):
        return "YES"
    else: return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
