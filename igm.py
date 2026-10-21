import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for IGM
# 
# Australian Informatics Olympiad 2026
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of delegates.
N = 0
# A contains the delegates' importance values. The list starts from 0.
A = []

# Read the number of delegates and their importance values.
N = int(input().strip())
A = list(map(int, input().strip().split()))

lowest = min(A)
startIndex = A.index(lowest)

canDo = "YES"

for i in range(N-1):
    currIdx = (startIndex + i) % N
    nxt = (currIdx + 1) % N
    if A[currIdx] > A[nxt]:
        canDo = "NO"

print(canDo)
