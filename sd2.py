from math import inf

#
# Solution Template for Sunday Drive II
#
# Australian Informatics Olympiad 2026
#
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# Read the street length and volume limits.
street_length = int(input().strip())
volume_limits = list(map(int, input().strip().split()))

forward_max = [0] * street_length
forward_max[0] = min(volume_limits[0], 1)
for pos in range(1, street_length):
    forward_max[pos] = min(volume_limits[pos], forward_max[pos - 1] + 1)

backward_max = [0] * street_length
backward_max[street_length - 1] = volume_limits[street_length - 1]
for pos in range(street_length - 2, -1, -1):
    backward_max[pos] = min(volume_limits[pos], backward_max[pos + 1] + 1)

print(sum(min(forward_max[pos], backward_max[pos]) for pos in range(street_length)))