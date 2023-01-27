import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    
    left_diagonal=0;
    right_diagonal=0;
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                
                left_diagonal+=arr[i][j];
                
            if ((i+j) == (len(arr)-1)):
                
                right_diagonal+=arr[i][j];

            
    return abs(left_diagonal-right_diagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
