# https://www.hackerrank.com/challenges/new-year-chaos/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    # Shift all values by one so position and index both starts from 0
    # i.e. [1 2 3 4 5] becomes [0 1 2 3 4]
    queue = [num - 1 for num in q]
    for current_pos, sticker in enumerate(queue):
        shifted = sticker - current_pos
        # If any sticker has shifted by more than two places, return will print
        # "Too chaotic" and abort the function
        if shifted > 2:
            print("Too chaotic")
            return
        # When a bribe happens, a person with a sticker number larger moves forward
        # i.e. [1 2 3 5 4]
        # As a result, for each sticker number, by summing up the number of people
        # with a larger sticker number that is in front of it, we can get the total
        # number of bribes
        #
        # Moreover, since each person can only bribe twice, for each sticker number,
        # we can reduce the lookup by only checking between the current position and
        # the (original + 1) position
        #
        # Now to put this into code
        for pos in range(max([0, (sticker - 1)]), current_pos):
             if queue[pos] > sticker:
                 bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
