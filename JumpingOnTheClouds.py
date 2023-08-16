# Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud while avoiding thunderheads.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i <= len(c)-1:
        print(str(i) + ", " + str(c[i]))
        if i == len(c)-1:
            print("i=" + str(len(c)-1))
            break
        elif i == len(c)-2:
            if c[i+1] == 0:
                i += 1
                jumps += 1
                print("Last Cumulus " + str(i) + " " + str(jumps))
            else:
                i += 1
                jumps += 1
                print("Last Thunderhead " + str(i))
        else:
            if c[i+1] == 0 and c[i+2] == 1:
                i += 1
                jumps += 1
                print("Cumulus " + str(i) + " " + str(jumps))
            elif c[i+2] == 0:
                i += 2
                jumps += 1
                print("Skip Cumulus " + str(i) + " " + str(jumps))
            else:
                i += 1
                jumps += 1
                print("Thunderhead " + str(i))
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
