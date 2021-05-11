# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
# This solution will result in timeout for many test cases

#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    for i in range(len(expenditure)):
        if i + 1 <= d:
            continue
        if i + 1 > d:
            median = statistics.median(expenditure[i-d:i])
            if expenditure[i] >= median * 2:
                notifications += 1
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
