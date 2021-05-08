# https://www.hackerrank.com/challenges/count-triplets-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    ans = 0
    values = defaultdict(lambda: 0)
    pairs = defaultdict(lambda: 0)

    # By walking the array in reverse we are able to do this in one pass
    for i in reversed(arr):
        # These two ifs would effectively
        # 1. add occurence of i*r, i*r*r to ans by checking pairs
        # 2. add occurence of i, i*r to pairs by checking values
        if i*r in pairs:
            ans += pairs[i*r]
        if i*r in values:
            pairs[i] += values[i*r]
        # This assignment must be after the previous two if conditions
        # to handle r = 1 edge case
        values[i] += 1

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

