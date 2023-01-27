#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    x,z,y=0,0,0
    for i in range(0,len(arr)):
        if arr[i]>0:
            x = x + 1
        elif arr[i]<0:
            y = y + 1
        else:
            z = z + 1
    print(x/len(arr)) #percentage of positive numbers
    print(y/len(arr)) #percentage of negative numbers
    print(z/len(arr)) #percentage of zeros

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
