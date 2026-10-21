import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Jump on Platforms
# 
# Australian Informatics Olympiad 2026
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of platforms.
N = 0
# P contains the platform positions. The list starts from 0, so the positions
# are P[0] to P[N-1].
P = []

# Read the number of platforms and their positions.
N = int(input().strip())
P = list(map(int, input().strip().split()))

longestDistance = 0

for i in range(N-1):
    distance = abs(P[i] - P[i+1])
    if distance > longestDistance:
        longestDistance = distance

answer = longestDistance

# Write the answer.
print(answer)
