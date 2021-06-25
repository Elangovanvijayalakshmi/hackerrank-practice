#github.com/Elangovanvijayalakshmi

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(ar):
    # Write your code here
    i=0
    minsum=0
    maxsum=0
    list1=[]
    num1=sum(ar)-ar[0]
    num2=sum(ar)-ar[1]
    num3=sum(ar)-ar[2]
    num4=sum(ar)-ar[3]
    num5=sum(ar)-ar[4]
    list1.append(num1)
    list1.append(num2)
    list1.append(num3)
    list1.append(num4)
    list1.append(num5)                

    
    minsum=min(list1)
    maxsum=max(list1)       
    print (minsum,maxsum)
               

        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
