#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    from collections import Counter
    n = len(a) + len(b)
    a = Counter(a)
    b = Counter(b)
    common_string_cnt = 0
    
    for key, val in a.items():
        tmp = b.get(key, 0)
        common_string_cnt += min(tmp, val)
    
    return n - 2*common_string_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
