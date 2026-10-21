import sys
sys.setrecursionlimit(1000000000)
import statistics

#
# Solution Template for Prime Minister
# 
# Australian Informatics Olympiad 2026
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of citizens and K is the money available.
N = 0
K = 0
# A contains the citizens' initial wealth in sorted order. The list starts from
# 0.
A = []

# Read N, K, and the initial wealth values.
N, K = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

A.sort() # just in case

answer = 0

if K == 0:
    answer = statistics.median(A)
    print(answer)
    exit()

median_index = N // 2

def cost(target_value, A, median_index):
    total = 0
    for wealth in A[median_index:]:
        if wealth < target_value:
            total += (target_value - wealth)
    return total

low = A[median_index]
high = max(A) + K + 1

while low < high:
    guess = (low + high + 1) // 2 # try the midddle

    dollars_needed = cost(guess, A, median_index)
    if dollars_needed <= K:
        low = guess
    else:
        high = guess - 1

# Write the answer.
print(low)
