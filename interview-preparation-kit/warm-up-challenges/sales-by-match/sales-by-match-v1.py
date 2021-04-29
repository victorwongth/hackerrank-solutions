# https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):

    # First count the number of socks per color
    categories = {}
    for category in ar:
        try:
            categories[category] += 1
        except KeyError:
            categories[category] = 1

    # Next sume upe the number of pairs per color
    pairs = 0
    for _, value in categories.items():
        pairs += int(value/2)

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
