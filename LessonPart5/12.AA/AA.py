import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(m):
#     start, dest = map(int, input().split())
#     graph[start][dest] = 1
#     graph[dest][start] = 1

for i in range(m):
    start, dest, cost = map(int, input().split())
    graph[start][dest] = cost

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
    print()
