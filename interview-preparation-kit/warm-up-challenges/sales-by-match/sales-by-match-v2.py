# https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):

    # If you are familiar with list comprehension,
    # this is equivalent to
    #
    # for sock_type in set(ar):
    #   pairs += int(ar.count(sock_type) / 2)
    #
    pairs = sum[int(ar.count(sock_type) / 2) for sock_type in set(ar)]

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
