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
        # This while loop swaps the current array[i] value with the element
        # at position i until array[i] = i which effectively gives O(n)
        while array[i] != i:
            current_value = array[i]
            array[i] = array[current_value]
            array[current_value] = current_value
            res += 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close(
