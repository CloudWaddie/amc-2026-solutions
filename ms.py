import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Mundane Square
# 
# Australian Informatics Olympiad 2026
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the grid size and K is the maximum value in a cell.
grid_size = 0
max_value = 0
# R and C contain the target row and column sums. The lists start from 0.
rowSum = []
colSum = []

# Read N, K, and the target row and column sums.
grid_size, max_value = map(int, input().strip().split())
rowSum = list(map(int, input().strip().split()))
colSum = list(map(int, input().strip().split()))

class Edge:
    def __init__(self, to, capacity, reverse):
        self.to = to
        self.capacity = capacity
        self.reverse = reverse

def add_edge(a, b, capacity):
    forward = Edge(b, capacity, len(graph[b]))
    backward = Edge(a, 0, len(graph[a]))
    graph[a].append(forward)
    graph[b].append(backward)


def bfs(graph, source):
    level = [-1] * len(graph)
    level[source] = 0
    queue = [source]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for e in graph[u]:
            if e.capacity > 0 and level[e.to] == -1:
                level[e.to] = level[u] + 1
                queue.append(e.to)
    return level

def dfs(graph, u, sink, f, level, it):
    if u == sink:
        return f
    while it[u] < len(graph[u]):
        e = graph[u][it[u]]
        if e.capacity > 0 and level[u] + 1 == level[e.to]:
            d = dfs(graph, e.to, sink, min(f, e.capacity), level, it)
            if d > 0:
                e.capacity -= d
                graph[e.to][e.reverse].capacity += d
                return d
        it[u] += 1
    return 0



if sum(rowSum) != sum(colSum):
    print("NO")
    exit()

possible = True
upper = grid_size * max_value

for r in rowSum:
    if r < 0 or r > upper:
        print("NO")
        exit()

if possible:
    for c in colSum:
        if c < 0 or c > upper:
            print("NO")
            exit()

if not possible:
    print("NO")
    exit()

# lets make a graph. a source for enter and sink for exit.

N = grid_size
source = 0
sink = 2 * N + 1

total_nodes = 2 * N + 2


graph = [[] for _ in range(total_nodes)]

for i in range(N):
    add_edge(source, 1+i, rowSum[i])

cell_edge = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        cell_edge[i][j] = len(graph[1 + i])
        add_edge(1+i, 1+N+j, max_value)

for j in range(N):
    add_edge(1+N+j, sink, colSum[j])

total = sum(rowSum)
flow = 0
INF = 10**18
while True:
    level = bfs(graph, source)
    if level[sink] == -1:
        break
    it = [0] * total_nodes
    while True:
        pushed = dfs(graph, source, sink, INF, level, it)
        if pushed == 0:
            break
        flow += pushed

if flow != total:
    print("NO")
    exit()

grid = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        grid[i][j] = max_value - graph[1 + i][cell_edge[i][j]].capacity

print("YES")
for row in grid:
    print(" ".join(map(str, row)))
