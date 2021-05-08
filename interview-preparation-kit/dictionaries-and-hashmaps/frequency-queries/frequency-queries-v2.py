# https://www.hackerrank.com/challenges/frequency-queries/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    # If we only use a occurence dictionary, we have to perform a lookup whenever operation == 3
    # By maintaining both occurence and frequency we can reduce the amount of lookup as the
    # frequency dictionary is much smaller
    freq = defaultdict(lambda: 0)
    occurence = defaultdict(lambda: 0)
    ans = []
    for q in queries:
        operation = q[0]
        value = q[1]
        if operation == 3:
            if freq[value] != 0:
                ans.append(1)
            else:
                ans.append(0)
            continue
        
        freq[occurence[value]] -= 1
        if operation == 1:
            occurence[value] += 1
        elif operation == 2:
            if occurence[value] >= 1:
                occurence[value] -= 1
        freq[occurence[value]] += 1
        
    return(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
