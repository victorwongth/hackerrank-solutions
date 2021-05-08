# https://www.hackerrank.com/challenges/frequency-queries/problem
# This solution will timeout for 2 of the test cases

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    # This solution stores the occurence of each value in a dictionary
    # then perform a lookup whenever neccesary
    occurence = defaultdict(lambda: 0)
    ans = []
    for q in queries:
        operation = q[0]
        value = q[1]
        if operation == 1:
            occurence[value] += 1
        elif operation == 2:
            if occurence[value] >= 1:
                occurence[value] -= 1
        elif operation == 3:
            if value in occurence.values():
                ans.append(1)
            else:
                ans.append(0)
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

    fptr.close(
