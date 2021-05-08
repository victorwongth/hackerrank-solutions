# https://www.hackerrank.com/challenges/count-triplets-1/problem
# This solution works but will time out

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):

    # First count occurence of each int and store its index in this format
    # d = {'1': [0, 2, 3], '4': [1, 5], ...}
    values = defaultdict(lambda: [])
    for i in range(len(arr)):
        values[str(arr[i])].append(i)

    # Then for each value check whether
    # 1. the value * r and value * r * r exist
    # 2. whether those values have indexes larger than that of current value
    ans = 0
    for value, indexes in values.items():
        r1 = int(value) * r
        r2 = int(value) * r * r
        if str(r1) not in values.keys() or str(r2) not in values.keys():
            continue
        for index in indexes:
            for r1_index in values[str(r1)]:
                for r2_index in values[str(r2)]:
                    if r2_index > r1_index and r1_index > index:
                        ans += 1
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

