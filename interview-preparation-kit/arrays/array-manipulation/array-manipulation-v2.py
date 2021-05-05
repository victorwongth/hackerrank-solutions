# https://www.hackerrank.com/challenges/crush/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # This is an improvement over v1 where instead of manipulating every
    # element per query, we recognize the fact that these two statements are
    # identical
    # 1. add k to all elements between index a and b (what we used in v1)
    # 2. add k to all elements after a then deducting b from all elements
    #   after b (what we will use in v2)
    # As a result track the largest value by summing any addition or deduction
    # of k at any index
    # i.e. For input
    # 10 3
    # [1, 3, 100]
    # [2, 5, 100]
    # [6, 8, 100]
    # We can construct a list
    # [100, 100, 100, -100, 100, -100, 0, 0, -100 ,0]
    # Now when we sum it from left to right while comparing the current value
    # and the previous maximum value, we can get the result
    #
    # Write your code here
    l = [0] * n

    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        l[a] += k
        # Index would go out of range if b = n
        if b != n:
            l[b] -= k

    max_value = 0
    current_value = 0
    for value in l:
        current_value += value
        if current_value > max_value:
            max_value += current_value

    return(max_value)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

