#!/bin/python3
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    up = 0
    down = 0
    valleys = 0
    valley_eligible = False
    for i in range(steps):
        step = path[i]
        if str(step) == "D":
            down += 1
            valley_eligible = True
        else:
            up += 1
            print(str(step))
            print("U " + str(up))
            print("D " + str(down))
            print("V " + str(valleys))
            print("----")
            if up == down and valley_eligible:
                # if up>1 and down>1:
                valleys += 1
                up = 0
                down = 0
                valley_eligible = False
                print("New valleys " + str(valleys))
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
