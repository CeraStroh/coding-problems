# Given an integer, n, find and print the number of letter a's in the first n letters of an infinite string.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    sLength = len(s)
    sIndex = 0
    count = 0
    remainderCount = 0
    if s == ("a" * sLength):
        result = n
    else:
        for index in range(sLength):
            if s[index] == "a":
                count += 1
        # print("there are " + str(count) + " a's in s")
        sCount = int(n / sLength)
        # print(str(sCount) + "=" + str(n) + "/" + str(sLength))
        result = sCount * count
        # print("result " + str(result))
        sRemainder = n % sLength
        if sRemainder !=0:
            # print("remainder")
            for j in range(sRemainder):
                if s[j] == "a":
                    remainderCount += 1
                    # print("remainderCount " + str(remainderCount))
        result += remainderCount
        # print(str(result))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
