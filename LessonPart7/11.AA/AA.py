# 플로이드 워샬 알고리즘

import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

dis = [[1000] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dis[i][i] = 0

for i in range(m):
    src, dest, cost = map(int, input().split())
    dis[src][dest] = cost

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dis[i][j] == 1000:
            print("M", end=" ")
        else:
            print(dis[i][j], end=" ")
    print()
