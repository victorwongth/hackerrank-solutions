# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
# This solution avoid calculating median repeatedly by maintaining a dictionary
# for easier lookup of the (d // 2) and (d // 2 + 1) expenditure within a period

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def findValueFromIndex(freq, index):
    count = 0
    for i in range(0, 201):
        if freq[i] != 0:
            count += freq[i]
        if count >= index:
            return i


def activityNotifications(expenditure, d):
    notifications = 0
    freq = defaultdict(lambda: 0)
    for i in range(len(expenditure)):
        day = i + 1
        # Days before d populates the freq dictionary
        # i.e. for 5, 4, [1, 2, 5, 1, ...]
        # freq = {'1': 2, '2': 1, '5': 1}
        if day <= d:
            freq[expenditure[i]] += 1
            continue
        # Starting d + 1 we can use the findValueFromIndex function to lookup
        # the expenditure value (i.e. key of freq) that is the (d // 2) or
        # (d // 2 + 1) entry with a non-zero value
        if day > d:
            if d % 2 == 0:
                threshold = findValueFromIndex(freq, d // 2) + findValueFromIndex(freq, d // 2 + 1)
            else:
                threshold = findValueFromIndex(freq, d // 2 + 1) * 2
            if expenditure[i] >= threshold:
                notifications += 1
            # Finally we add the entry of today and remove the out-dated entry
            freq[expenditure[i]] += 1
            freq[expenditure[i-d]] -= 1
    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

