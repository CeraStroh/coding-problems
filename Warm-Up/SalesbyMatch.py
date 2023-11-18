#!/bin/python3
# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar.sort()
    print("sorted array: " + str(ar))
    sum = 1
    count = 0
    for i in range(0, n-1):
        if ar[i] == ar[i+1]:
            sum += 1
        else:
            count = int(count + sum/2)
            sum = 1
    count = int(count + sum/2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
