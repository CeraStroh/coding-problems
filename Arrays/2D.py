#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    sumArray = []
    smallSum = 0
    for a in range(4):
        for i in range(4):
            for j in range(3):
                print("i,j = " + str(i) + "," + str(j))
                x, y = j+i, i+a
                smallSum += arr[x][y]
                print(str(x) + ", " + str(y) + " = " + str(arr[x][y]))
                print("ss= " + str(smallSum))
            smallSum += arr[i+1][i+1]
            for j in range(3):
                x, y = j+i, i+a+2
                smallSum += arr[x][y]
                print(str(x) + ", " + str(y) + " = " + str(smallSum))
            sumArray.append(smallSum)
            print("restart")
    return max(sumArray)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
