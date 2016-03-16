#!/bin/python
### Problem Statement ###
### Given an array of integers, calculate which fraction of the elements are positive, negative, and zeroes, respectively. ###
### Print the decimal value of each fraction.####

import sys
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
count_neg = 0
count_pos = 0
count_zero = 0
for i in arr:
    if i < 0:
        count_neg =  count_neg + 1
    elif i > 0:
        count_pos =  count_pos + 1  
    else:
        count_zero =  count_zero + 1
print count_pos/float(n)
print count_neg/float(n)
print count_zero/float(n)