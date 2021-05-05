# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
# This solution works but the complexity is O(n^2) so test cases
# will timeout

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    # First shift all elements by one so index matches the value
    array = [d-1 for d in arr]

    res = 0
    for i in range(len(array)):
        if array[i] != i:
            for j in range(i, len(array)):
                if array[j] == i:
                    array[j] = array[i]
                    array[i] = i
                    res += 1

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
