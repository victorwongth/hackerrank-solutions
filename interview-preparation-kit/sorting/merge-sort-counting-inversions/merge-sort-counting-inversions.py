# https://www.hackerrank.com/challenges/ctci-merge-sort/problem
# Bubblesort would be too slow and will timeout most of the test cases
# This solution requires the understanding of mergesort

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    return(mergeSort(arr, 0))

def mergeSort(arr, count):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        count = mergeSort(left, count)
        count = mergeSort(right, count)

        # This aims to help visualize the below algorithm for given
        # left = [2,4,6] and right = [1,5,5]
        # i j k count arr
        # 0 1 1 3 [1]
        # 1 1 2 3 [1,2]
        # 2 1 3 3 [1,2,4]
        # 2 2 4 4 [1,2,4,5]
        # 2 3 5 5 [1,2,4,5,5]
        # 3 3 5 5 [1,2,4,5,5,6]

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                arr[k] = right[j]
                # Swaps only occur when elements are moved from the right
                # array to the left array
                count += len(left) - i
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
