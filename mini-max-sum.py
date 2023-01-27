#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):

    minimum=min(arr)
    maximum=max(arr)
    summ=sum(arr)
    
    print(summ-maximum , summ-minimum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)