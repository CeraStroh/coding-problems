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
    aNum = 0
    sLength = len(s)
    for i in range(sLength):
        if s[i] == "a":
            aNum += 1
    divide = n/sLength
    print(str(divide) + "," + str(aNum))
    if isinstance(divide, float):
        occurences = divide * aNum
        print(str(occurences))
        occurences = round(occurences)
    else:
        occurences = int(divide * aNum)
    print(str(occurences))
    return occurences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
