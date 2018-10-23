#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# Uses partial tail recursion for optimization that was not taken care of in algorithm. 
def rotLeft(a, d):
    def rotateHelper(a, d, count):
        if d == count:
            return a
        else:
            first = a.pop(0)
            a.append(first)
            count += 1
            # print(a)
            return rotateHelper(a, d, count)
    return rotateHelper(a, d, 0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
